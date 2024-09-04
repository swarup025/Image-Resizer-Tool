import cv2

path=input("enter the image path")

if path is None :
    print("Error : Image path no Load.....!")

else :
    width=int(input("enter the image with"))
    height=int(input("enter the image height"))

    img=cv2.imread(path,1)
    img2=cv2.resize(img,(width,height))
    cv2.imshow("original Image", img)
    cv2.imshow("output image",img2)
    k=cv2.waitKey(0)

if(k == ord("s")):
    cv2.imwrite(r"C:\Users\swaru\Desktop\project\ output.jpeg", img2)  # Notice the 'r' before the string
    print("Image successfully saved......")
    
else :
    cv2.destroyAllWindows()
