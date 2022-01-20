def trap(height: list[int]) -> int:
    beams = []
    total = 0
    i = 0
    last = 0
    for i in range(len(height)):
        if height[i] > height[last]:
            diff = height[i] - height[last]
            while beams:
                beam = beams.pop()
                if height[last] <= beam[0] and beam[1] <= height[i]:
                    total += (beam[1] - beam[0]) * (last - beam[2])
                elif height[i] > beam[0]:
                    beam_a, beam_b = (beam[0], height[i], beam[2]), (height[i], beam[1], beam[2])
                    total += (beam_a[1] - beam_a[0]) * (last - beam_a[2])
                    beams.append(beam_b)
                    break
                else:
                    beams.append(beam)
                    break
                    
                    
        elif height[i] < height[last]:
            beams.append((height[i], height[last], last))
                
        last = i
        
    return total