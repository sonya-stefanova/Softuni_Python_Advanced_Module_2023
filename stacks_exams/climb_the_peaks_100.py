from collections import deque

portion = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
days_counter = 1

peaks = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza"
}

conquered_peaks = []


while portion and stamina and days_counter <=7:
    curr_portion = portion.pop()
    current_stamina = stamina.popleft()
    total = curr_portion + current_stamina

    for height, peak_name in peaks.items():

        if total >= height:
            conquered_peaks.append(peak_name)
            peaks.pop(height)

        days_counter += 1
        break


if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(f"{peak}")