Chapter Summmary:
  We learned how to encrypt and decrypt meessages using the transposition cipher, substitution cipher, and the Vignere cipher.

List and describe 3 basic string methods.
  1. astring.center(w) returns a string surroundeed by spacees to make astring w characters long
  2. astring.find(item) returns the index of the first occurence of an item in astring, or uses -1 if not found
  3. astring.upper() returns astring in all uppercase letters

Describe the 3 simple algorithms for encryption that we covered in this lesson
  The Transposition Cipher scrambles letters and separates them into two different groups of evens and odds.
  
  The Substitution Cipher is self explanatory and substitutes one letter with another in the alphabet. It is easy to crack using logic since some letters appear far more often in the alphabet.
  
  The Vignere Cipher is an improved Substitution Cipher. It allows multiple mappings of the same letter and makes it much more difficult to crack.

Identify the type of encryption the following algorithim is implementing:

def encrypt(plainText ,key):  
  alphabet = "abcdefghijklmnopqrstuvwxyz"  
  plainText = plainText.lower ()  
  cipherText = ""  

  for ch in plainText:  
      idx = alphabet.find(ch)  
      cipherText = cipherText + key[idx]  
  return cipherText
It is using a substitution Cipher

Identify the type of encryption the following algorithim is implementing :

def scramble2Encrypt(plainText):  
  evenChars = ""  
  oddChars = ""  
  charCount = 0  

  for ch in plainText:  
      if charCount % 2 == 0:  
          evenChars = evenChars + ch  
      else:  
          oddChars = oddChars + ch  
    charCount = charCount + 1  
  cipherText = oddChars + evenChars  
  return cipherText
It is using the Transposition Cipher
 
