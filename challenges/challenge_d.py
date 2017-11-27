"""
Given the list of domains in domains.txt, complete the following tasks:

1.  Output a file called tlds.txt that contains an alphabetical list of 
unique tlds in the domains list and the number of occurrences of each, 
separated by a colon. e.g:

com:97
nz:200
uk:108

2.  Assign each domain a score by assigning each letter a numerical 
value according to its position in the alphabet multiplied by its position 
in the domain and summing those values. Non-letter characters (such as 
numbers, hyphens, and periods) are worth nothing. For example:

abacus.com 
1*1 = 1, 2*2 = 4,  1*3 = 3, 3*4 = 12, 21*5 = 105, 19*6 = 114, 0*7 = 0, 
3*8 = 24, 15*9 = 135, 13*10 = 130 (so abacus.com has a total score of 528)

Output a file called domain_scores.txt that contains a list of domains sorted by their domain score (in descending order), with each line containing the domain and score, separated by a colon. For example:

abacus.com:528
ebay.com:339

"""

import operator


def assign_domain_points(domain_list_file_name):
    domain_dict = {}
    with open(domain_list_file_name) as domain_list_file_object:
        for domain in get_next_domain(domain_list_file_object):
            if domain:
                domain = domain[:-1]
                domain_dict[domain] = get_domain_value(domain)
            else:
                break
        sorted_domains = sort_domains(domain_dict)
        write_to_file(sorted_domains)


def write_to_file(sorted_domains):
    with open("domain_scores.txt ", "w+") as domain_scores:
        try:
            for domain, score in sorted_domains:
                domain_scores.write("{}:{}\n".format(domain, score))
        finally:
            domain_scores.close()


def sort_domains(domain_dict):
    return sorted(domain_dict.items(), key=operator.itemgetter(1), reverse=True)


def get_next_domain(domain_list_file):
    for line in domain_list_file:
        yield line


def get_domain_list(domain):
    return list(domain)


def get_domain_value(domain):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    domain_list = get_domain_list(domain)
    domain_value = 0
    for index, char in enumerate(domain_list):
        domain_placement_value = index + 1
        alphabet_placement_value = 0
        alphabet_placement_value = alphabet.index(char.lower()) + 1 if char.isalpha() else 0
        character_value = domain_placement_value * alphabet_placement_value
        domain_value += character_value
    return domain_value


if __name__ == "__main__":
    assign_domain_points(domain_list_file_name="domains.txt")
