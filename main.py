from graph import Graph

MENU = "MENU \nadiciona vertice <key> \nadiciona aresta <src> <dest> [weight] \nmostra \nsair"
WORDS_MENU = ['vertice', "aresta"]

def graph_function(sentece: str, graph: Graph):
    option = sentece.split(' ')
    if(option[1] in WORDS_MENU):
        if(option[1] == 'vertice'):
            graph.add_vertex(option[2])
        else:
            if len(option) > 4:
                graph.add_edge(option[2], option[3], option[4])
            else:
                graph.add_edge(option[2], option[3])

def main():
    graph = Graph()
    is_running = True
    print(MENU)
    while(is_running):
        sentece = input('\nO que você gostaria de fazer? ')
        if sentece.lower().startswith('adiciona'):
            graph_function(sentece, graph)
        elif sentece.lower().startswith('mostra'):
            graph.show()
        elif sentece.lower().startswith('visualiza'):
            graph.plot()
        elif sentece.lower() == 'sair':
            is_running = False
        else:
            print("Está opção não existe, escolha uma das que estão presente no menu!")

if __name__ == "__main__":
    main()

