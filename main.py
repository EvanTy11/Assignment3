import Retriever
class main:


    def main():
        r1 = Retriever.Retriever("https://api.openweathermap.org/data/2.5/weather?","d252374e5abf5d1d0c777e96c85263c1")
        r1.send()
        r1.print()

    if __name__ == '__main__':
        main()