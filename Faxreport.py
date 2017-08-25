import xml.etree.ElementTree as ET
tree = ET.parse("export_job_logResponse.xml")
root = tree.getroot()
links = root.findall("{http://www.kyoceramita.com/ws/km-wsdl/log/log_information}export_job_log")
print(links)