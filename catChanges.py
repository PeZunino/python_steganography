import cv2 as cv
import numpy as np


def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]


def gerar_mensagem(mensagem):
    lista = []
    for m in mensagem:
        val = ord(m)
        bits = bitfield(val)

        if len(bits) < 8:
            for a in range(8-len(bits)):
                bits.insert(0,0)
        lista.append(bits)
    arr = np.array(lista)
    arr = arr.flatten()
    return arr


def converter_mensagem(saida):
    bits = np.array(saida)
    mensagem_out = ''
    bits = bits.reshape((int(len(saida)/8), 8))
    for b in bits:
        sum = 0
        for i in range(8):
            sum += b[i]*(2**(7-i))
        mensagem_out += chr(sum)
    return mensagem_out


def get_red_pixels_values_as_binary() -> np.ndarray:
    red_pixels_found = 0
    lista = []

    print('Changing red value to binary')
    for line in range(cat_image_arr.shape[0]):
        for column in range(cat_image_arr.shape[1]):
            if red_pixels_found < pixels_needed_count:
                print(cat_image_arr[line, column, 2], end=" ")
                if cat_image_arr[line, column, 2] % 2 == 0:
                    lista.append(0)
                else:
                    lista.append(1)

                print("-> ", lista[red_pixels_found])
                red_pixels_found += 1
    print('Red values changed to ', lista)

    arr = np.array(lista)
    return arr


def encrypt_message_on_image() -> None:
    message_bits_count = 0
    for line in range(cat_image_arr.shape[0]):
        for column in range(cat_image_arr.shape[1]):
            if message_bits_count < len(red_pixels_values):
                cat_image_arr[line, column, 2] = message_as_binary[message_bits_count]
                message_bits_count += 1
            else:
                continue


def get_message_from_image():
    pixels_found = 0
    binary_bits_founds = np.zeros(pixels_needed_count, dtype=int)

    for line in range(cat_image_arr.shape[0]):
        for column in range(cat_image_arr.shape[1]):
            if pixels_found < pixels_needed_count:
                binary_bits_founds[pixels_found] = cat_image_arr[line, column, 2]
                pixels_found += 1
    return binary_bits_founds


raw_message = input('Type your message: ')

message_as_binary = gerar_mensagem(raw_message)
print('Message as Binary ', message_as_binary)

pixels_needed_count = len(message_as_binary)
print('Gonna need ', pixels_needed_count)

cat_image = cv.imread('Photos/cat.jpg')
cat_image_arr = np.array(cat_image)

red_pixels_values = get_red_pixels_values_as_binary()

encrypt_message_on_image()

encrypted_message = get_message_from_image()

print("Encrypted message: ", encrypted_message)

decrypted_message = converter_mensagem(encrypted_message)

print("Decrypted message: ", decrypted_message)

