import psutil
import optparse


def coco_find(watch_list):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        for target in watch_list:
            if p.name() == target:
                print(p.name())
                print(p.children())


def input_parser(input):
    result = []
    if ',' in input:
        result = input.split(',')
    else:
        result.append(input)
    return result


def main():
    parser = optparse.OptionParser("usage%prog "+"[OPTIONS]")
    parser.add_option("-p", dest="pname", type="string", help="Compact Mode: -p process_name")
    parser.add_option("-n", dest="pid", type="string", help="Specify BroLog Name: -n process_id")
    (options, args) = parser.parse_args()
    pname=options.pname
    pid=options.pid

    if pname is not None:
        pname_list = input_parser(pname)
        print('your watch list {}'.format(pname_list))
        coco_find(pname_list)
    elif pid is not None:
        pid_list = input_parser(pid)
    else:
        print parser.usage
        exit(0)






if __name__ == '__main__':
    main()
