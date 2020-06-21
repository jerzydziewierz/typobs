def run():
    """
    parses the arguments and runs to_typora() function
    :return: spews darnduff to the console.
    """
    default_source_path = r'/home/mib07150/git/2020_portfolio/PMBOK templates/'
    import argparse
    import os
    parser = argparse.ArgumentParser(
        description='convert all links inside markdown files to the [text](link) style used by http://typora.io',
        epilog='have a beautiful day!'
        )

    parser.add_argument('-d', '--default_path', action="store_true", dest='use_default_path', default=False, help=f'use the default hard-coded path of "{default_source_path}"')
    parser.add_argument('-p', '--path', action="store", metavar='path', dest='path', type=str,
                        help='top-level source path (explored recursively)')
    arguments = parser.parse_args()
    if arguments.use_default_path:
        source_path = default_source_path
        print(f'using default path of "{source_path}"')
    else:
        if arguments.path is not None:
            source_path = arguments.path
            print(f'using supplied path of "{source_path}"')
        else:
            source_path = f'{os.getcwd()}/'
            print(f'using current folder path (pwd) : "{source_path}"')

    to_typora(source_path=source_path)


def to_typora(source_path=r'/home/mib07150/git/2020_portfolio/PMBOK templates/'):
    """
    converts all the links inside the .md files to typora style, [text](link)
    :param source_path: where to start
    :return: spews darnduff to the console.
    """
    source_folder_firstchar = len(source_path)
    import os

    # create the list of files of interest in the source_folder

    fname_list = []
    fpurename_list = []
    for root, d_names, f_names in os.walk(source_path):
        for f in f_names:
            if ".md" in f[-3:] and not ".trash" in root:
                # fname.append(os.path.join(root, f))
                ths_fname = os.path.join(root, f)[source_folder_firstchar:]
                print(f'"{ths_fname}" is "{f[:-3]}"')
                fname_list.append(ths_fname)
                fpurename_list.append(f[:-3])

    import re

    # This pattern matches [[something]]
    # note that link descriptors are not supported here.


    # convert [[x]] links to [x](path_to\x.md) ===============

    pattern_basic_obslink_getter = r'\[\[ *(?P<link>.+?) *\]\]'
    re_link = re.compile(pattern_basic_obslink_getter)


    file_idx = 0
    for file_idx in range(len(fname_list)):
        filename = os.path.join(source_path, fname_list[file_idx])
        filename_short = fname_list[file_idx]
        # prepare link_prefix so that the files being in subfolders get correct up-folder path prefix

        link_prefix = ''
        file_depth = filename_short.count('/')
        for depth_idx in range(file_depth):
            link_prefix = f'{link_prefix}../'

        print(f'processing ({file_idx})[{file_depth}]: "{filename_short}"...')
        content = open(filename).read()

        last_pos = 0
        while True:
            matched = re_link.search(content)
            if not matched:
                print('no more matches...', end='')
                break
            link_string = matched.groupdict()['link']
            new_pos = matched.span()[1]
            matched_string = content[matched.span()[0]:matched.span()[1]]
            # check if this is a file in the list
            f_candidate = None
            for f_candidate in fname_list:
                if link_string in f_candidate:
                    break
            if f_candidate is not None:
                # print(f'{z.span()} [[{link_string}]] -> {f_candidate}')
                # create the replacement, commonmark link
                link_file_string = re.sub(r" ", "%20", f_candidate)  # replace spaces with "%20"
                commonmark_link = f'[{link_string}]({link_prefix}{link_file_string})'
                print(f'replacing {matched.span()} [[{link_string}]] -> {commonmark_link}')
                # replace the old style link in the source text with new style link
                content = content.replace(matched_string, commonmark_link)
                last_pos = new_pos  # move on
        print('writing...', end='')
        f = open(filename, "w")
        f.write(content)
        f.close()
        print('done.')
        print('')
