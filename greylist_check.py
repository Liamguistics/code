import sys
import codecs

hws_fn= sys.argv[1] # list of headwords (plus id plus posp plus existing examples)
greylist_fn = sys.argv[2]
out_fn = sys.argv[3]

def contains_greylist (greylist, my_string):
        """
        for removing MWE greylists not handled by GDEX
        input: list of grey MWE
        output: matches reported in extra column if concordance contains any term in greylist
        """
        my_string = my_string.replace(',','')
        my_string = my_string.replace('!','')
        my_string = my_string.replace(':','')
        my_string = my_string.replace(';','')
        my_string = my_string.replace(';','')
        my_string = my_string.replace('.','')
        my_string = my_string.replace('"','')
        my_string = my_string.replace('"','')
        my_string = my_string.replace(' l\'',' ')
        my_string = re.sub(r'\t\t.*$', '', my_string)
        my_string = " "+my_string+" "
        for term in greylist:
                term = " "+term+" "
                if term.lower() in my_string.lower():
                        return 1
                        break

def load_list_from_file(list_fn):
        """
        input: txt file, one list item per line
        output: list
        """

        l = []
        with codecs.open(list_fn, 'r','utf-8') as list_f:
                for line in list_f:
                        line = line.rstrip()
                        l.append(line)

        return l

def main (hws_fn, greylist_fn,out_fn):
        # read in greylist
        greylist = load_list_from_file(greylist_fn)
        with codecs.open(out_fn, 'w', 'utf-8') as out_f:
                with codecs.open(hws_fn, 'r', 'utf-8') as in_f:
                        # read in each line of headword file
                        for line in in_f:
                                line = line.rstrip()
                                parts = line.split("\t")
                                start = parts[0]+"\t"+parts[1]+"\t"+parts[2]+"\t"
                                hw = parts[0]
                                exa = parts[1]
                                # check if headword is in greylist
                                if contains_greylist(greylist,hw): #append greylist item in hw
                                        out_f.write('\n'.join([line + '\tgreylist item in hw' for parts in line]))
                                elif contains_greylist(greylist,exa): #append greylist item in exa
                                        out_f.write('\n'.join([line + '\tgreylist item in example' for parts in line]))
                                else:
                                        out_f.write('\n'.join([line + '\tno match' for parts in line]))

if __name__ == "__main__":
                main (hws_fn, greylist_fn, out_fn)