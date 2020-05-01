#load_xml.py
import xml.etree.ElementTree as ET
import concurrent.futures
import glob, os, datetime, logging, timeit

if os.path.exists("load_xml_b.log"):
    os.remove("load_xml_b.log")

logging.basicConfig(level=logging.DEBUG, filename='load_xml_b.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
start = datetime.datetime.now()
logging.info(f'Start time is {start}')

list_run = 1
dict_run = 1

#initialized lists/dicts
files = []
div0_d = {}
div1_d = {}
interp_d = {}
xptr_d = {}
join_d = {}
persName_d = {}
rs_d = {}

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

def gather_info_dict(xf):
    #logging.info(f'XML file being interpreted is {xf}')
    tree = ET.parse(xf)
    root = tree.getroot()
    for rec in root.iter('div0'):
        #div0.append((str(rec.attrib.get("type")), str(rec.attrib.get("id"))))
        div0_d[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))
    for rec in root.iter('div1'):
        #div1.append((str(rec.attrib.get("type")), str(rec.attrib.get("id"))))
        div1_d[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))
    for rec in root.iter('interp'):
        #interp.append((str(rec.attrib.get("inst")), str(rec.attrib.get("type")), str(rec.attrib.get("value"))))
        interp_d[str(rec.attrib.get("inst"))] = [str(rec.attrib.get("type")), str(rec.attrib.get("value"))]
    for rec in root.iter('xptr'):
        #xptr.append((str(rec.attrib.get("type")), str(rec.attrib.get("doc"))))
        xptr_d[str(rec.attrib.get("doc"))] = str(rec.attrib.get("type"))
    #join is going to be different, some join xml tags don't have everything so we will input default values
    for rec in root.iter('join'):
        #join.append((str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("id", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown"))))
        join_d[str(rec.attrib.get("id", "unknown"))] = [str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown"))]
    for rec in root.iter('persName'):
        #persName.append((str(rec.attrib.get("id")), str(rec.attrib.get("type"))))
        persName_d[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))
    for rec in root.iter('rs'):
        #rs.append((str(rec.attrib.get("id")), str(rec.attrib.get("type"))))
        rs_d[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))

def gather_info_list(xf):
    #logging.info(f'XML file being interpreted is {xf}')
    tree = ET.parse(xf)
    root = tree.getroot()
    for rec in root.iter('div0'):
        div0.append((str(rec.attrib.get("type")), str(rec.attrib.get("id"))))
        #div0[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))
    for rec in root.iter('div1'):
        div1.append((str(rec.attrib.get("type")), str(rec.attrib.get("id"))))
        #div1[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))
    for rec in root.iter('interp'):
        interp.append((str(rec.attrib.get("inst")), str(rec.attrib.get("type")), str(rec.attrib.get("value"))))
        #interp[str(rec.attrib.get("inst"))] = [str(rec.attrib.get("type")), str(rec.attrib.get("value"))]
    for rec in root.iter('xptr'):
        #xptr.append((str(rec.attrib.get("type")), str(rec.attrib.get("doc"))))
        xptr[str(rec.attrib.get("doc"))] = str(rec.attrib.get("type"))
    #join is going to be different, some join xml tags don't have everything so we will input default values
    for rec in root.iter('join'):
        join.append((str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("id", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown"))))
        #join[str(rec.attrib.get("id", "unknown"))] = [str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown"))]
    for rec in root.iter('persName'):
        persName.append((str(rec.attrib.get("id")), str(rec.attrib.get("type"))))
        #persName[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))
    for rec in root.iter('rs'):
        rs.append((str(rec.attrib.get("id")), str(rec.attrib.get("type"))))
        #rs[str(rec.attrib.get("id"))] = str(rec.attrib.get("type"))

for parent_dir in dirs:
    for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
        files.append(xml_file)

#multithreading
def multi_dict():
    global dict_run
    div0_d.clear()
    div1_d.clear()
    interp_d.clear()
    xptr_d.clear()
    join_d.clear()
    persName_d.clear()
    rs_d.clear()
    logging.info(f'MULTI DICT RUN #{str(dict_run)}')
    logging.info(f'Time of run is: {datetime.datetime.now()}')
    dict_run+=1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gather_info_dict, files)

def multi_list():
    global list_run
    div0.clear()
    div1.clear()
    interp.clear()
    xptr.clear()
    join.clear()
    persName.clear()
    rs.clear()
    logging.info(f'MULTI LIST RUN #{str(list_run)}')
    logging.info(f'Time of run is: {datetime.datetime.now()}')
    list_run+=1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gather_info_list, files)

test_list = timeit.timeit(stmt = multi_dict, 
                    number = 10) 

test_dict = timeit.timeit(stmt = multi_list, 
                    number = 10) 

#print(test_list)
#print(test_dict)

logging.info(f'DICT TIME IS: {test_dict}')
logging.info(f'LIST TIME IS: {test_list}')

#logging.info(f'div0 is: {len(div0)}')
#logging.info(f'div1 is: {len(div1)}')
#logging.info(f'interp is: {len(interp)}')
#logging.info(f'join is: {len(join)}')
#logging.info(f'persName is: {len(persName)}')
#logging.info(f'xptr is: {len(xptr)}')
#logging.info(f'rs is: {len(rs)}')

logging.info(f'Start time is {start}')
end = datetime.datetime.now()
logging.info(f'End time is {end}')
delta = end - start
logging.info(f'Elapsed time is {delta}')
