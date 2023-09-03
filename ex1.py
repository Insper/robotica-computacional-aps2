from module import ImageModule
import cv2
import numpy as np

class Atividade1(): # Essa classe deve herdar da classe ImageModule
    def __init__(self):
        # Inicializar a classe pai

        # Definir aqui os atributos da classe
        self.f = 0
        self.ciano = {
            'lower': None,
            'upper': None
        }

        self.magenta = {
            'lower': None,
            'upper': None
        }

        # Configure o kernel para operações morfológicas

    def encontrar_foco(self, D: float, H: float, h: float) -> float:
        """Não mude ou renomeie esta função
        Entradas:
        D - distancia real da câmera até o objeto [m]
        H - a distancia real entre os circulos [m]
        h - a distancia virtual entre os circulos [px]
        Saída:
        f - a distância focal da câmera [px]
        """
        f = None

        return f
    
    def encontrar_centros(self, bgr: np.ndarray) -> (tuple, tuple):
        """Não mude ou renomeie esta função
        Entrada:
            bgr - imagem de entrada no formato BGR
        Saída:
            centro_ciano - centro do circulo ciano no formato (X,Y)
            centro_magenta - centro do circulo magenta no formato (X,Y)
        """
        centro_ciano = None
        centro_magenta = None

        return centro_ciano, centro_magenta
    
    def calcular_h(self, centro_ciano: tuple, centro_magenta: tuple) -> float:
        """Não mude ou renomeie esta função
        Entradas:
            centro_ciano - ponto no formato (X,Y)
            centro_magenta - ponto no formato (X,Y)
        Saída:
            distancia - a distancia Euclidiana entre os pontos de entrada 
        """
        
        distancia = None
        return distancia

    def encontrar_D(self, f: float, H: float, h: float) -> float:
        """Não mude ou renomeie esta função
        Entrada:
            f - a distância focal da câmera [px]
            H - a distancia real entre os circulos [m]
            h - a distancia virtual entre os circulos [px]
        Saída:
            D - distancia real da câmera até o objeto [m]
        """
        D = None
        return D

    def calcular_theta(self, centro_ciano: tuple, centro_magenta: tuple) -> float:
        """Não mude ou renomeie esta função
            Deve calcular o angulo, em graus, entre o vetor formato com os centros do circulos e a vertical.
        Entradas:
            centro_ciano - centro do círculo ciano no formato (X,Y)
            centro_magenta - centro do círculo magenta no formato (X,Y)
        Saídas:
            angulo - ângulo com a vertical em graus
        """
        angulo = None
    
        return angulo

    def escrever_texto(self, bgr: np.ndarray, distancia: float, angulo: float) -> np.ndarray:
        """Não mude ou renomeie esta função
        Entradas:
            bgr - imagem de entrada no formato BGR
            distancia - distancia real da câmera até o objeto [m]
            angulo - ângulo com a vertical em graus
        Saída:
            bgr - imagem de entrada com o texto desenhado
        """
        # Escreva o texto na imagem
        return bgr

    def calibration(self, bgr: np.ndarray) -> np.ndarray:
        """Esta função deve ser processar o frame de entrada chamando as funções necessárias para executar o exercicio 1 da APS 2. 
        Crie quantas funções auxiliares achar necessário dentro dessa classe ou dentro da classe ImageModule.

        Se desejar pode retornar uma máscara durante o desenvolvimento para facilitar a visualização

        Args:
            bgr (np.ndarray): Frame de entrada

        Returns:
            bgr (np.ndarray): Frame com o exercicio 1 desenhado
        """
        bgr, D, angulo, h = self.run(bgr)
        self.f = None

        return bgr, D, angulo, h, self.f

    def run(self, bgr: np.ndarray) -> np.ndarray:
        """Esta função deve ser processar o frame de entrada chamando as funções necessárias para executar o exercicio 1 da APS 2. 
        Crie quantas funções auxiliares achar necessário dentro dessa classe ou dentro da classe ImageModule.

        Se desejar pode retornar uma máscara durante o desenvolvimento para facilitar a visualização

        Args:
            bgr (np.ndarray): Frame de entrada

        Returns:
            bgr (np.ndarray): Frame com o exercicio 1 desenhado
            h (float): Distancia virtual entre os circulos [px]
            f (float): Distância focal da câmera [px]
            angulo (float): Ângulo com a vertical em graus
        """
        # Esta função deve ser implementada para executar o exercicio 1
        return None


def rodar_frame():
    RodaAtividade = Atividade1()
    
    bgr = cv2.imread("img/calib01.jpg") # Escolha aqui a imagem que deseja usar para testar
    # bgr = cv2.imread("img/angulo01.jpg")
    # bgr = cv2.imread("img/angulo02.jpg")
    # bgr = cv2.imread("img/angulo03.jpg")
    # bgr = cv2.imread("img/angulo04.jpg")

    bgr, D, angulo, h, f = RodaAtividade.calibration(bgr)

    # Mostre a imagem final usando o OpenCV
    # ...


def rodar_webcam():
    RodaAtividade = Atividade1()
    bgr = cv2.imread("img/calib01.jpg") # Escolha aqui a imagem que deseja usar para testar
    bgr, D, angulo, h, f = RodaAtividade.calibration(bgr)

    cap = cv2.VideoCapture(0)

    while True:
        ret, bgr = cap.read()
        bgr, D, angulo, h = RodaAtividade.run(bgr)

        cv2.imshow("Imagem", bgr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
def main():
    # Selecione se deseja rodar seu codigo com uma imagem ou um video:

    rodar_frame()
    # rodar_webcam()


if __name__ == "__main__":
    main()