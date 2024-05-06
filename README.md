
# Password_Manager
Password Manager Program

# Graphical User Interface (GUI) application using the tkinter and various libraries in Python

The application allows users to generate a secure password and save website login details (website, email, username, and password) to a file named data.txt.

Time Complexity:

generate_password() function: The time complexity of this function primarily depends on the length of the generated password and the number of iterations required to satisfy all the conditions. The while loop will continue generating passwords until it meets all the specified conditions (at least one lowercase, one uppercase, three digits, and two symbols). The loop may iterate multiple times until it finds a suitable password, but it's essential to note that the number of iterations is limited since the character space for the password is relatively small. In practice, it usually requires a constant number of iterations to find a valid password. Hence, the time complexity can be approximated as O(1).

![Screenshot 2024-05-05 175345](https://github.com/shanshee/Flash_Card_App/assets/135793255/a8ffc39c-2b1c-4473-8527-ed0734f40c30)

add_password() function: The time complexity of this function is generally constant because it involves basic operations like getting the website, email, and password values from the Entry widgets, writing the data to a file, and clearing the Entry widgets. These operations do not depend on the size of the data being processed, so the time complexity is O(1).

Overall, the time complexity of the provided code is O(1), which means the time required for execution is constant and not dependent on the size of the input.


Space Complexity:

generate_password() function: The space complexity of this function mainly depends on the space used to store the generated password and the symbols and alphabet lists. Given that the length variable (12 in this case) specifies a fixed length for the password, its size is constant. The "symbols" list and alphabet string are also fixed and do not depend on the input size. Hence, the space complexity of this function is O(1).

![Screenshot 2024-05-05 175411](https://github.com/shanshee/Flash_Card_App/assets/135793255/2bdb1cae-1ab8-431a-a632-924da0f9bc78)

add_password() function: The space complexity of this function is also O(1) because it uses a constant amount of space to store the website, email, and password values, regardless of the size of the data.

Overall, the space complexity of the code is O(1), which means the amount of memory used is constant and not dependent on the size of the input or the number of iterations in the generate_password() function.

In summary, the code has both time and space complexities of O(1), making it efficient and suitable for most practical purposes, as the execution time and memory usage remain constant regardless of the input size.
