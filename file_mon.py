import optparse
from filecmp import dircmp
import filecmp

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print "diff_file {} found in {} and {}".format(name, dcmp.left, dcmp.right)
        if dcmp.left_only != dcmp.right_only:
            print "src dir: {}".format(dcmp.left)
            print "src files: {}".format(dcmp.left_only)
            print "dst dir: {}".format(dcmp.right)
            print "dst files: {}".format(dcmp.right_only)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


def main():
    parser = optparse.OptionParser("usage%prog "+"[OPTIONS]")
    parser.add_option("-s", dest="src", type="string", help="Specify src absolute path")
    parser.add_option("-d", dest="dst", type="string", help="Specify dst absolute path")
    (options, args) = parser.parse_args()
    src=options.src
    dst=options.dst

    if (src and dst) is not None:
        dcmp = dircmp(src, dst) 
        print_diff_files(dcmp)
    else:
        print parser.usage
        exit(0)


if __name__ == '__main__':
    main()
