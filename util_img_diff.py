import cv2
import numpy as np

def subtract_images(image1_path, image2_path, output_path):
    # 讀取圖片
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    
    # 檢查兩張圖片是否大小相同
    if img1.shape != img2.shape:
        raise ValueError("兩張圖片大小不相同")

    # 計算圖片相減
    result = cv2.subtract(img1, img2)

    # 將結果保存到指定路徑
    cv2.imwrite(output_path, result)
    
    return result

if __name__ == "__main__":
    # 測試函數
    image2_path = 'imgs\depth_frame_3.png'
    image1_path = 'imgs\depth_frame_0.png'
    output_path = 'diff.png'

    result = subtract_images(image1_path, image2_path, output_path)

    # 顯示輸出圖片
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
