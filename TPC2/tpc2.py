import re
from dataclasses import dataclass
from pprint import pprint
from sys import stdin


@dataclass
class music:
    nome: str
    desc: str
    ano: str
    periodo: str
    compositor: str
    duracao: str
    _id: str

def dataset(csv: str) -> set[music]:
    res = list()

    matches = re.findall(r"[^ \n]+?(?:[^;]+;){6}[^\n]+", csv)

    for i in range(1, len(matches)):
        elems = re.findall(r"[^;]+", matches[i])

        if len(elems) == 7:
            res.append(music(elems[0],
                                   elems[1],
                                   elems[2],
                                   elems[3],
                                   elems[4],
                                   elems[5],
                                   elems[6]))

    return res

def compositoresOrdenados(dataset: list[music]) -> set[str]:
    res = set()

    for i in dataset:
        res.add(i.compositor)
    return sorted(res)

def contaPeriodo(dataset: list[music]) -> dict[str, int]:
    res = dict()
    for i in dataset:
        count = res.get(i.periodo, 0)
        res[i.periodo] = count + 1

def musicaPPeriodo(dataset: list[music]) -> dict[str, int]:
    res = dict()

    for i in dataset:
        m= res.get(i.periodo, [])
        m.append(i.nome)
        res[i.periodo] = m

    
    for names in res.values():
        names.sort()
    return res

def main():
    csv = open("obras.csv", "r", encoding='utf-8').read()
    dts = dataset(csv)

    print("Lista ordenada alfabeticamente dos compositores musicais:")
    pprint(compositoresOrdenados(dts))
    print("\n")

    print("Obras catalogadas em cada período:")
    pprint(contaPeriodo(dts))
    print("\n")

    print("Lista alfabética dos títulos das obras de cada período:")
    pprint(musicaPPeriodo(dts))
    print("\n")


if __name__ == "__main__":
    main()