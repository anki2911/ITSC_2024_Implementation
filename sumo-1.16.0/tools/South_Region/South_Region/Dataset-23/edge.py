import traci
import xml.etree.ElementTree as EleT

def convert_coordinates(xml_file, output_file):
    tree = EleT.parse(xml_file)
    root = tree.getroot()
    traci.start(["sumo", "-c", "osm.sumocfg"])

    with open(output_file, "w") as f:
        edges = root.findall("edge")

        for edge in edges:
            edge_from = edge.get("from")
            edge_to = edge.get("to")

            if edge_from is not None and edge_to is not None:
                edge_id = edge.get("id")
                lanes = edge.findall("lane")

                for lane in lanes:
                    lane_id=lane.get("id")
                    lane_length = traci.lane.getLength(lane_id)
                f.write(f"{edge_id} {edge_from} {edge_to} {lane_length}\n")

    traci.close()

xml_file = "osm.net.xml"
output_file = "Edge_Details.txt"
convert_coordinates(xml_file, output_file)
