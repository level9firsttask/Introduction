from zeep import Client
import xmltodict, json
client = Client(wsdl="http://dev.usbooking.org/us/UnitedSolutions?wsdl")
code = client.service.FlightAvailability('GULFTN','PASSWORD','PLZ161','KTM','BWA','5-1-2021','','O','NP',1,0,'49.25.14.12')
# data_dict = xmltodict.parse(code)

with open("data.xml", "w") as xml_file:
    xml_file.write(code)
    xml_file.close()


data_dict = xmltodict.parse(code)
json_data = json.dumps(data_dict)
for i in json_data:
    print(i)