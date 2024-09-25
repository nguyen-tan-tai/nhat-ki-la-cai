import os

root_dir = "."
presentation_dir = f'{root_dir}/presentations'
build_dir = f'{root_dir}/build'

for p in os.listdir(presentation_dir):
    s = []
    md_dir = f"{presentation_dir}/{p}"
    for md in os.listdir(md_dir):
        f = f"{md_dir}/{md}"
        mdf = open(f, "r", encoding='utf-8')
        s.append(mdf.read())

    tf = open(f"{root_dir}/template.html", "r", encoding='utf-8')
    t = tf.read()
    c = t.replace("${SLIDES}", "\n".join(s))

    sf = open(f"{build_dir}/{p}.html", "w", encoding='utf-8')
    sf.write(c)

