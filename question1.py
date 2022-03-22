from pydoc import doc
import importlib


def doc_to_html(module, file_name):
    importlib.import_module(module)
    f = open(file_name, "w")
    f.write(str(dir(module)))
    doc(module, output=f)
    f.close()


if __name__ == '__main__':
    doc_to_html("question3", "mydoc.html")