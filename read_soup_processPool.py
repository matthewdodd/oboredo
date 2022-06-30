#read_soup.py

from bs4 import BeautifulSoup
import re, glob, os, datetime, logging
import concurrent.futures

logging.basicConfig(level=logging.DEBUG, filename='./logs/read_soup_processPool.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

#initialize
dirs = ['./ordinarysAccounts/','./sessionsPapers/']
#dirs = ['./']
files = []
main_list_div0 = []
main_list_div1 = []
main_list_interp = []
main_list_join = []
main_list_rs = []

def gather_info(xf):
    logging.info(f'XML file being interpreted is {xf}')
    list_div0 = []
    list_div1 = []
    list_interp = []
    list_join = []
    list_rs = []
    with open(xf, encoding = "latin-1") as xml_file:
        soup = BeautifulSoup(xml_file,'xml')
        div0 = soup.find_all('div0')
        div1 = soup.find_all('div1')
        interp = soup.find_all('interp')
        join = soup.find_all('join')
        rs = soup.find_all('rs')
        for value in div0:
            div0_id = str(value['id'])
            div0_type = str(value['type'])
            div0_tmp = '"'+div0_id+'"'+','+'"'+div0_type+'"'
            list_div0.append(div0_tmp)
        for value in div1:
            div1_id = str(value['id'])
            div1_type = str(value['type'])
            div1_tmp = '"'+div1_id+'"'+','+'"'+div1_type+'"'
            list_div1.append(div1_tmp)
        for value in interp:
            interp_inst = str(value['inst'])
            interp_type = str(value['type'])
            interp_value = str(value['value'])
            interp_tmp = '"'+interp_inst+'"'+','+'"'+interp_type+'"'+','+'"'+interp_value+'"'
            list_interp.append(interp_tmp)
        for value in join:
            join_result = str(value['result'])
            join_targets = str(value['targets'])
            join_tmp = '"'+join_result+'"'+','+'"'+join_targets+'"'
            list_join.append(join_tmp)
        for value in rs:
            rs_inst = str(value['id'])
            rs_type = str(value['type'])
            rs_value = re.sub('\\s+', ' ', str(value.text.strip().replace('\n','')))
            rs_tmp = '"'+rs_inst+'"'+','+'"'+rs_type+'"'+','+'"'+rs_value+'"'
            list_rs.append(rs_tmp)
    return list_div0, list_div1, list_interp, list_join, list_rs

def main():
    start = datetime.datetime.now()
    logging.info(f'Start time is {start}')

    #glob all the files
    for parent_dir in dirs:
      logging.info(f'got into dirs with {parent_dir}')
      for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
        logging.info(f'got into files with {xml_file}')
        files.append(xml_file)

    #multithreading gather info
    logging.info(f'Beginning data extraction execution')
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for r in executor.map(gather_info, files):
            main_list_div0.append(r[0])
            main_list_div1.append(r[1])
            main_list_interp.append(r[2])
            main_list_join.append(r[3])
            main_list_rs.append(r[4])
    logging.info(f'Data extraction completed')
    
    logging.info(f'Flattening lists for load')
    flat_list_div0 = [x for xs in main_list_div0 for x in xs]
    flat_list_div1 = [x for xs in main_list_div1 for x in xs]
    flat_list_interp = [x for xs in main_list_interp for x in xs]
    flat_list_join = [x for xs in main_list_join for x in xs]
    flat_list_rs = [x for xs in main_list_rs for x in xs]
    logging.info(f'Lists flattened')

    #output info
    logging.info(f'Outputting data to files')
    open('./output/list_div0.txt', 'w', encoding='utf-8').write('\n'.join(flat_list_div0))
    print('Done - div0: '+str(len(flat_list_div0)))
    open('./output/list_div1.txt', 'w', encoding='utf-8').write('\n'.join(flat_list_div1))
    print('Done - div1: '+str(len(flat_list_div1)))
    open('./output/list_interp.txt', 'w', encoding='utf-8').write(''.join(flat_list_interp))
    print('Done - interp: '+str(len(flat_list_interp)))
    open('./output/list_join.txt', 'w', encoding='utf-8').write(''.join(flat_list_join))
    print('Done - join: '+str(len(flat_list_join)))
    open('./output/list_rs.txt', 'w', encoding='utf-8').write(''.join(flat_list_rs))
    print('Done - rs: '+str(len(flat_list_rs)))
    logging.info(f'Data successfully output to files')

    end = datetime.datetime.now()
    logging.info(f'End time is {end}')
    delta = end - start
    logging.info(f'Total Elapsed time is {delta}')

if __name__ == '__main__':
    main()