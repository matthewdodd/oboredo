#load_xml.py
import xml.etree.ElementTree as ET
import concurrent.futures
import glob, os, datetime, logging

if os.path.exists("read_xml.log"):
    os.remove("read_xml.log")

logging.basicConfig(level=logging.DEBUG, filename='read_xml.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
start = datetime.datetime.now()
logging.info(f'Start time is {start}')

#initialized lists
files = []
div0 = []
div1 = []
interp = []
xptr = []
join = []
persName = []
rs = []

#defined lists
dirs = ['C:/temp/obo/OBO_XML_72/sessionsPapers', 'C:/temp/obo/OBO_XML_72/ordinarysAccounts']
tag = ['div0', 'div1', 'interp', 'xptr', 'join', 'persName', 'rs']

def gather_info_list(xf):
    logging.info(f'XML file being interpreted is {xf}')
    tree = ET.parse(xf)
    root = tree.getroot()
    for rec in root.iter('div0'):
        div0.append((str(rec.attrib.get("type")), str(rec.attrib.get("id"))))
    for rec in root.iter('div1'):
        div1.append((str(rec.attrib.get("type")), str(rec.attrib.get("id"))))
    for rec in root.iter('interp'):
        interp.append((str(rec.attrib.get("inst")), str(rec.attrib.get("type")), str(rec.attrib.get("value"))))
    for rec in root.iter('xptr'):
        xptr[str(rec.attrib.get("doc"))] = str(rec.attrib.get("type"))
    #join is going to be different, some join xml tags don't have everything so we will input default values
    for rec in root.iter('join'):
        join.append((str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("id", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown"))))
    for rec in root.iter('persName'):
        persName.append((str(rec.attrib.get("id")), str(rec.attrib.get("type"))))
    for rec in root.iter('rs'):
        rs.append((str(rec.attrib.get("id")), str(rec.attrib.get("type"))))

for parent_dir in dirs:
    for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
        files.append(xml_file)

#multithreading
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(gather_info_list, files)

logging.info(f'div0 is: {len(div0)}')
logging.info(f'div1 is: {len(div1)}')
logging.info(f'interp is: {len(interp)}')
logging.info(f'join is: {len(join)}')
logging.info(f'persName is: {len(persName)}')
logging.info(f'xptr is: {len(xptr)}')
logging.info(f'rs is: {len(rs)}')

logging.info(f'Start time is {start}')
end = datetime.datetime.now()
logging.info(f'End time is {end}')
delta = end - start
logging.info(f'Elapsed time is {delta}')
