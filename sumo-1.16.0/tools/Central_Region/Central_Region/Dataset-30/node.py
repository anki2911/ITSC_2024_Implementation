import traci
import xml.etree.ElementTree as EleT

def convert_coordinates(xml_file, output_file):
    tree = EleT.parse(xml_file)
    root = tree.getroot()
    traci.start(["sumo", "-c", "osm.sumocfg"])

    with open(output_file, "w") as f:
        junctions = root.findall("junction")

        for junction in junctions:
            junction_id = junction.get("id")
            x = float(junction.get("x"))
            y = float(junction.get("y"))

            lon, lat = traci.simulation.convertGeo(x, y)
            f.write(f"{junction_id} {lat} {lon}\n")

    traci.close()

xml_file = "osm.net.xml"
output_file = "Node.txt"
convert_coordinates(xml_file, output_file)
