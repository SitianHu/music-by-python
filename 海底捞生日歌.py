from music21 import stream, note, chord, tempo, meter, instrument

# 创建乐谱
score = stream.Score()
part1 = stream.Part()
part2 = stream.Part()
part3 = stream.Part()
part4 = stream.Part()
part5 = stream.Part()

# 设置速度、节拍和乐器
part1.insert(0, instrument.Violin())  # 将 part1 设置为小提琴声音
part1.append(tempo.MetronomeMark(number=90))
part1.append(meter.TimeSignature('4/4'))

part2.insert(0, instrument.Guitar())  # 将 part2 设置为吉他声音
part2.append(tempo.MetronomeMark(number=120))
part2.append(meter.TimeSignature('4/4'))

part3.insert(0, instrument.Guitar())  # 将 part3 设置为吉他声音
part3.append(tempo.MetronomeMark(number=120))
part3.append(meter.TimeSignature('4/4'))

part4.insert(0, instrument.Guitar())  # 将 part4 设置为吉他声音
part4.append(tempo.MetronomeMark(number=120))
part4.append(meter.TimeSignature('4/4'))

part5.insert(0, instrument.Piano())  # 将 part5 设置为钢琴声音
part5.append(tempo.MetronomeMark(number=120))
part5.append(meter.TimeSignature('4/4'))

# 伴奏部分
accompaniment1 = stream.Part()
accompaniment1.insert(0, instrument.Piano())
# accompaniment1.getElementsByClass(instrument.Instrument)[0].midiChannel = 0
accompaniment2 = stream.Part()
accompaniment2.insert(0, instrument.Violin()) 


# 示例：用具体旋律代替随机音符
melody1 = [
    ('G3', 0.5), ('G3', 0.5), ('A3', 1), ('G3', 1), ('c4', 1), ('B3', 2),
    ('G3', 0.5), ('G3', 0.5), ('A3', 1), ('G3', 1), ('d4', 1), ('c4', 2),
    ('G3', 0.5), ('G3', 0.5), ('g4', 1), ('e4', 1), ('c4', 1), ('B3', 1), ('A3', 2),
    ('F4', 0.5), ('F4', 0.5), ('E4', 1), ('c4', 1), ('d4', 1), ('c4', 3)]
melody2 = [
    ('C4', 0.25), ('D4', 0.25),
    ('E4', 0.5), ('C4', 0.25), ('D4', 0.25), ('E4', 0.5), ('C4', 0.5), ('D4', 1), ('G4', 1),
    ('C4', 0.5), ('A3', 0.25), ('B3', 0.25), ('C4', 0.5), ('A3', 0.5), ('B3', 1), ('E4', 1),
    ('A3', 0.5), ('F3', 0.25), ('G3', 0.25), ('A3', 0.5), ('F3', 0.5), ('G3', 1), ('C4', 1),
    ('F3', 0.25), ('E3', 0.25), ('F3', 0.25), ('G3', 0.25), ('A3', 0.25), ('G3', 0.25), ('A3', 0.25), ('B3', 0.25),
    ('C4', 0.25), ('B3', 0.25), ('C4', 0.25), ('D4', 0.25), ('E4', 0.25), ('D4', 0.25), ('E4', 0.25), ('F4', 0.25), 
    ('G4', 2), (0, 1), (0, 1)
]
melody3 = [
    ('E4', 0.5), ('G4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 1), (0, 1),
    ('D4', 0.5), ('G4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 1), (0, 1),
    ('C4', 0.5), ('C4', 0.5), ('C4', 0.5), ('C4', 0.5), ('C4', 1), ('C5', 1),
    ('B4', 0.5), ('G4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 2),
    ('A4', 0.5), ('C5', 0.5), ('C5', 0.5), ('D5', 0.5), ('C5', 1), ('C5', 0.5), ('A4', 0.5),
    ('G4', 0.5), ('A4', 0.5), ('A4', 0.5), ('G4', 0.5), ('E4', 2), 
    ('F4', 0.75), ('F4', 0.75), ('E4', 0.5), ('F4', 0.5), ('E4', 1), ('C4', 0.5), 
    ('D4', 2), (0, 1), (0, 1),
    ('E4', 0.5), ('G4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 1), (0, 1),
    ('D4', 0.5), ('G4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 1), (0, 1),
    ('C4', 0.5), ('C4', 0.5), ('C4', 0.5), ('C4', 0.5), ('C4', 1), ('C5', 1),
    ('B4', 0.5), ('G4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 2),
    ('A4', 0.5), ('C5', 0.5), ('C5', 0.5), ('D5', 0.5), ('C5', 1), ('C5', 0.5), ('A4', 0.5),
    ('G4', 0.5), ('E5', 0.5), ('E5', 0.5), ('D5', 0.5), ('C5', 2), 
    ('A4', 0.75), ('A4', 0.75), ('G4', 0.5), ('A4', 0.5), ('A4', 1), ('C5', 0.5), 
    ('D5', 2), (0, 1), (0, 0.5), ('G4', 0.5)
]
melody4 = [
    ('E5', 1), ('C5', 0.75), ('D5', 0.25), ('E5', 1), ('C5', 1),
    ('D5', 0.5), (0, 0.5), ('G4', 0.5), (0, 0.5), ('G4', 1), (0, 0.5), ('E4', 0.5),
    ('C5', 1), ('A4', 0.75), ('B4', 0.25), ('C5', 1), ('A4', 1),
    ('B4', 0.5), (0, 0.5), ('G5', 0.5), (0, 0.5), ('G5', 2), 
    ('F5', 1), ('F5', 0.75), ('E5', 0.25), ('D5', 1), ('E5', 0.75), ('F5', 0.25),
    ('E5', 0.5), (0, 0.5), ('D5', 0.5), (0, 0.5), ('C5', 1), ('A4', 1),
    ('C5', 1), ('C5', 0.75), ('A4', 0.25), ('C5', 1), ('D5', 0.5), ('E5', 0.5),
    ('D5', 3), (0, 0.5), ('G4', 0.5),
    ('E5', 1), ('C5', 0.75), ('D5', 0.25), ('E5', 1), ('C5', 0.75), ('C5', 0.25),
    ('D5', 0.5), (0, 0.5), ('G4', 0.5), (0, 0.5), ('G4', 1), (0, 0.5), ('E4', 0.5),
    ('C5', 1), ('A4', 0.75), ('B4', 0.25), ('C5', 1), ('A4', 0.75), ('A4', 0.25),
    ('B4', 0.5), (0, 0.5), ('G5', 0.5), (0, 0.5), ('G5', 2), 
    ('F5', 1), ('F5', 0.75), ('E5', 0.25), ('D5', 1), ('E5', 0.75), ('F5', 0.25),
    ('E5', 0.5), (0, 0.5), ('D5', 0.5), (0, 0.5), ('C5', 1), ('A4', 1),
    ('C5', 1), ('C5', 0.75), ('A4', 0.25), ('C5', 1), ('D5', 0.5), ('E5', 0.5),
    ('D5', 1), (0, 0.5), ('B4', 0.5), ('C5', 1), ('C5', 0.5), ('D5', 0.5),
    ('C5', 5), (0, 3)
]

# 计算第一个旋律的总时长
melody1_duration = sum(duration for _, duration in melody1)
melody2_duration = sum(duration for _, duration in melody2)
melody3_duration = sum(duration for _, duration in melody3)

# 添加第一个旋律
for pitch, duration in melody1:
    n = note.Note(pitch, quarterLength=duration)
    n.volume.velocity = 40  # 设置音量更轻
    part1.append(n)

# 在第二个旋律开始前添加等待时间
r1 = note.Rest(quarterLength=melody1_duration)
part2.append(r1)

r2 = note.Rest(quarterLength=melody1_duration + melody2_duration)
part3.append(r2)

r3 = note.Rest(quarterLength=melody1_duration + melody2_duration + melody3_duration)
part4.append(r3)
part5.append(r3)

# 添加第二个旋律
for pitch, duration in melody2:
    if pitch == 0:
        part2.append(note.Rest(quarterLength=duration))
    else:
        n = note.Note(pitch, quarterLength=duration)
        part2.append(n)

# 添加第三个旋律
for pitch, duration in melody3:
    if pitch == 0:
        part3.append(note.Rest(quarterLength=duration))
    else:
        n = note.Note(pitch, quarterLength=duration)
        part3.append(n)

# 添加第四个旋律
for pitch, duration in melody4:
    if pitch == 0:
        part4.append(note.Rest(quarterLength=duration))
    else:
        n = note.Note(pitch, quarterLength=duration)
        part4.append(n)

# 添加第五个旋律
for pitch, duration in melody4:
    if pitch == 0:
        part5.append(note.Rest(quarterLength=duration))
    else:
        n = note.Note(pitch, quarterLength=duration)
        part5.append(n)

accompaniment1.append(r2)
walking_bass = [
    ('C3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('C4', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5),  # C 小节
    ('G2', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5),  # G 小节
    ('A2', 0.5), (0, 0.5), ('E3', 0.5), (0, 0.5), ('A3', 0.5), (0, 0.5), ('E3', 0.5), (0, 0.5),  # Am 小节
    ('G2', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5),  # G 小节
    ('F2', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5), ('F3', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5),  # F 小节
    ('C3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('C4', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5),  # C 小节
    ('F2', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5), ('F3', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5), # F 小节
    ('G2', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5),  # G 小节
    ('C3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('C4', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5),  # C 小节
    ('G2', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5),  # G 小节
    ('A2', 0.5), (0, 0.5), ('E3', 0.5), (0, 0.5), ('A3', 0.5), (0, 0.5), ('E3', 0.5), (0, 0.5),  # Am 小节
    ('G2', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('D3', 0.5), (0, 0.5),  # G 小节
    ('F2', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5), ('F3', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5),  # F 小节
    ('C3', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5), ('C4', 0.5), (0, 0.5), ('G3', 0.5), (0, 0.5),  # C 小节
    ('F2', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5), ('F3', 0.5), (0, 0.5), ('C3', 0.5), (0, 0.5),  # F 小节
    ('G2', 1), ('D3', 1), ('G3', 1.5), (0, 0.5)  # G 小节
]

for pitch, dur in walking_bass:
    accompaniment1.append(note.Note(pitch, quarterLength=dur))
for n in accompaniment1.recurse().notes:   # 包含 Note 与 Chord
    n.volume.velocity = 45

accompaniment2.append(r3)  # 伴奏与第四部分同时开始

# 定义和弦进行
chord_progression = [
    ('C4', 'E4', 'G4'),  # C
    ('G3', 'B3', 'D4'),  # G
    ('A3', 'C4', 'E4'),  # Am
    ('G3', 'B3', 'D4'),  # G
    ('F3', 'A3', 'C4'),  # F
    ('C4', 'E4', 'G4'),  # C
    ('F3', 'A3', 'C4'),  # F
    ('G3', 'B3', 'D4'),  # G
    ('C4', 'E4', 'G4'),  # C
    ('G3', 'B3', 'D4'),  # G
    ('A3', 'C4', 'E4'),  # Am
    ('G3', 'B3', 'D4'),  # G
    ('F3', 'A3', 'C4'),  # F
    ('C4', 'E4', 'G4'),  # C
    ('F3', 'A3', 'C4'),  # F
    ('G3', 'B3', 'D4'),  # G
    ('C4', 'E4', 'G4'),  # C
]

# 定义节奏型
rhythm_pattern = [2, 1, 1]

# 直接生成和弦，不缓存对象
for pitches in chord_progression:
    for t in rhythm_pattern:
        accompaniment2.append(chord.Chord(pitches, quarterLength=t))
accompaniment2.append(chord.Chord(['C3', 'E3', 'G3'], quarterLength=4))

for el in accompaniment2.recurse().notes:
    el.volume.velocity = 50  # 给伴奏统一设一个力度


score.append(part1)
score.append(part2)
score.append(part3)
score.append(part4)
# score.append(part5)

score.append(accompaniment1)
score.append(accompaniment2)

# 保存为 MIDI 文件
score.write('midi', fp='海底捞生日歌.mid')

print("生成完毕！")