from music21 import stream, note, chord, tempo, meter, instrument
import random

# 创建乐谱
score = stream.Score()
part = stream.Part()

# 设置速度和节拍
part.append(tempo.MetronomeMark(number=110))
part.append(meter.TimeSignature('4/4'))

# 伴奏部分
accompaniment = stream.Part()
accompaniment.insert(0, instrument.Violin()) 

# 可选音符（C大调）
# scale_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# 随机生成旋律
# for _ in range(16):
#     pitch = random.choice(scale_notes)
#     duration = random.choice([0.25, 0.5, 1])  # 四分之一拍、半拍、一拍
#     n = note.Note(pitch, quarterLength=duration)
#     part.append(n)

# 示例：用具体旋律代替随机音符
melody = [
    ('C4', 1), ('C4', 1), ('G4', 1), ('G4', 1),
    ('A4', 1), ('A4', 1), ('G4', 2),
    ('F4', 1), ('F4', 1), ('E4', 1), ('E4', 1),
    ('D4', 1), ('D4', 1), ('C4', 2),
    ('G4', 1), ('G4', 1), ('F4', 1), ('F4', 1),
    ('E4', 1), ('E4', 1), ('D4', 2),
    ('G4', 1), ('G4', 1), ('F4', 1), ('F4', 1),
    ('E4', 1), ('E4', 1), ('D4', 2),
    ('C4', 1), ('C4', 1), ('G4', 1), ('G4', 1),
    ('A4', 1), ('A4', 1), ('G4', 2),
    ('F4', 1), ('F4', 1), ('E4', 1), ('E4', 1), 
    ('D4', 1), ('D4', 1), ('C4', 2),
    # ……这里继续填完整旋律
]

for pitch, duration in melody:
    n = note.Note(pitch, quarterLength=duration)
    part.append(n)

accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=4))
accompaniment.append(chord.Chord(['F3', 'A3', 'C4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['F3', 'A3', 'C4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['G3', 'B3', 'D4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))

accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['F3', 'A3', 'C4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['G3', 'B3', 'D4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['F3', 'A3', 'C4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['G3', 'B3', 'D4'], quarterLength=2))

accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=4))
accompaniment.append(chord.Chord(['F3', 'A3', 'C4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['F3', 'A3', 'C4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))
accompaniment.append(chord.Chord(['G3', 'B3', 'D4'], quarterLength=2))
accompaniment.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=2))

for el in accompaniment.recurse().notes:
    el.volume.velocity = 50  # 给伴奏统一设一个力度

# 加个和弦收尾
c_major = chord.Chord(['C4', 'E4', 'G4'], quarterLength=2)
g_major = chord.Chord(['G3', 'B3', 'D4'], quarterLength=2)
c_major_last = chord.Chord(['C3', 'E3', 'G3', 'C4'], quarterLength=4)
part.append(c_major)
part.append(g_major)
part.append(c_major_last)

score.append(part)
score.append(accompaniment)

# 保存为 MIDI 文件
score.write('midi', fp='小星星.mid')

print("生成完毕！")
