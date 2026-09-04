import cloudlink
from cloudlink import server
from cloudlink.server.protocols import clpv4, scratch
import asyncio
import os


class example_callbacks:
    def __init__(self, parent):
        self.parent = parent

    async def test1(self, client, message):
        print("Test1!")
        await asyncio.sleep(1)
        print("Test1 after one second!")

    async def test2(self, client, message):
        print("Test2!")
        await asyncio.sleep(1)
        print("Test2 after one second!")

    async def test3(self, client, message):
        print("Test3!")


class example_commands:
    def __init__(self, parent, protocol):

        # Creating custom commands - This example adds a custom command called "foobar".
        @server.on_command(cmd="foobar", schema=protocol.schema)
        async def foobar(client, message):
            print("Foobar!")

            # Reading the IP address of the client is as easy as calling get_client_ip from the clpv4 protocol object.
            print(protocol.get_client_ip(client))

            # In case you need to report a status code, use send_statuscode.
            protocol.send_statuscode(
                client=client,
                code=protocol.statuscodes.ok,
                message=message
            )


class example_events:
    def __init__(self):
        pass

    async def on_close(self, client):
        print("Client", client.id, "disconnected.")

    async def on_connect(self, client):
        print("Client", client.id, "connected.")


if __name__ == "__main__":
    # Initialize the server
    cl = cloudlink
    server = server()

    # Configure logging settings
    server.logging.basicConfig(
        level=server.logging.INFO
    )

    # Load protocols
    clpv4 = clpv4(server)
    scratch = scratch(server)

    # Load examples
    callbacks = example_callbacks(server)
    commands = example_commands(server, clpv4)
    events = example_events()

    # Binding callbacks - This example binds the "handshake" command with example callbacks.
    # You can bind as many functions as you want to a callback, but they must use async.
    # To bind callbacks to built-in methods (example: gmsg), see cloudlink.cl_methods.
    server.bind_callback(cmd="handshake", schema=clpv4.schema, method=callbacks.test1)
    server.bind_callback(cmd="handshake", schema=clpv4.schema, method=callbacks.test2)

    # Binding events - This example will print a client connect/disconnect message.
    # You can bind as many functions as you want to an event, but they must use async.
    # To see all possible events for the server, see cloudlink.events.
    server.bind_event(server.on_connect, events.on_connect)
    server.bind_event(server.on_disconnect, events.on_close)

    # You can also bind an event to a custom command.
    # Initialize SSL support
    # server.enable_ssl(certfile="cert.pem", keyfile="privkey.pem")

# Events
@server.on_connect
async def on_connect(client):
    print(client, "Connected!")
@server.on_disconnect
async def on_disconnect(client):
    print(client, "Disconnected!")
@server.on_error
async def on_error(client, errors):
    print(client, "encountered an error(s)", errors)
@server.on_protocol_identified(schema=clpv4.schema)
async def protocol_identified(client):
    print(client, "is using protocol", clpv4.schema)
@server.on_protocol_disconnect(schema=clpv4.schema)
async def protocol_disconnect(client):
    print(client, "Disconnected...")
@server.on_protocol_disconnect(schema=clpv4.schema)
async def protocol_disconnect(client):
    print(client, "Disconnected...")

# Commands and error handling
@server.on_exception(exception_type=server.exceptions.InvalidCommand, schema=clpv4.schema)
async def invalid_command(client, details):
    print(client, "sent an invalid command", details)
@server.on_exception(exception_type=server.exceptions.JSONError, schema=clpv4.schema)
async def json_exception(client, details):
    print(client, details)
# @server.empty_message(exception_type=server.exceptions.EmptyMessage, schema=clpv4.schema)
# async def empty_message(client, details):
#     print(client, details)

## GMINI
class MessageTriggerPlugin:
    def __init__(self, server_obj, protocol_obj):
        self.server = server_obj
        self.protocol = protocol_obj

        # Register the listener for the client-side command
        @self.server.on_command(cmd="broadcast_all", schema=self.protocol.schema)
        async def handle_broadcast_request(client, message):
            """
            client: The CloudLink client object who sent the message
            message: The raw dict received (contains keys like 'cmd', 'val', etc.)
            """
            # Extract what the client wants to broadcast from the 'val' key
            scene = message.get("val", "")
            try:
                with open("../../data/clientlookup/leveldata/"+str(scene)+".lvl") as lvlFile:
                    fileContent = lvlFile.read()
                    returnSceneData = fileContent
                print(f"Successfully loaded lvl file for scene {scene}")
            except:
                print(f"Failed to load lvl file for scene {scene}")
                pass

            # Structure the global message packet adhering to clpv4 specifications
            gmsg_packet = {
                "cmd": "gmsg",
                "val": returnSceneData
            }
            try:
                # This forcefully transmits the data downstream to the client
                server.send_packet(obj=client, message=gmsg_packet)
            except Exception as e:
                print(f"Failed to transmit to client {client}: {e}")


# Load your custom hook engine into the server context
MessageTriggerPlugin(server, clpv4)

# Start the server!
server.run(ip="localhost", port=3000)