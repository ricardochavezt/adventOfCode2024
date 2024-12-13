# Taken from https://topaz.github.io/paste/#XQAAAQCWBQAAAAAAAAAzHIoib6pMX4ickc1Mep93pgqtuV6rGB3/t2SKtfwDPt2r1515wsQUmcHJvxOgeyqU0+EtagUyY+1FBgQ3Yb+/Cc8VeSOxADCyiZJn2UXCr+fr6LdRoQ/ig56mck4ITPzK+0dtURzK7Q6pQDlVUYPZ7XCZSzP5+dU9tf6ewARHCQXt4MlIkBDQ2qCHZ4eEabRS3sHsBj446jOCtzgAgeJAka5qpvJFIMpWcz5ATyd3KrC/FfxwbeJtU1a+ZMPl7TTCgSncodwaPCj01ZufN5RoDKG/yBpDCm3G8Y6jKISWI2eZfny20go1rpcQk2W7/qmPPU6K7dLfnNldLCuslEV8wfpqK6zaCCAcruMN3WMTpWJ5165FWmD8VhgJv22BaLAoMxyk+yfBYshrzi49mlbhlbii+xo7HmCde7YuVHyOBWfABpwB703Kqw5zSUNb340EIje6sOjjnEEVt5rezHsHYVcRnL2Bo+SXkONLK6FbV5opw3TGJg8/qIt1/9sIKGaECTUjsMJlc9vLEyfwDhtP0nQ6sLblqOycJESLRXhIRF06S7qY4yxWDwt3vBoRy2h2NS6A5fo2t6sJ93Loio2nFgQCnaHDKrSsCZQwwBfefa/rC4VOP/+yPg7tEMjLzPdjxHxoAPJp9N54D2a5iVrth1CfGKXygmnJNCYyWuLcOU2x/yBsXLILnqC8Bkw+32ruRNDGM5GY3nf99vZM/y3PhNVCQXPxLOHimAfsUYi69cbBCBYprEiF+nENjAAIgVTdtASjuBEgTkN/40fdArCQ94deWpTC6jvLS04E7mdcvF31W+FUSl2MpFYOe0hr4sFkzOi62jPDIQJjUEcrzqr8fhG1NywCe+k41ZeHu//watpM
# (user nthistle on AoC's subreddit)

import fileinput

garden_plot_map = [line.strip() for line in fileinput.input()]
plot_ids = {}

def dfs(i, j, symbol, plot_id):
    if i in range(len(garden_plot_map)) and j in range(len(garden_plot_map[0])):
        if (i, j) in plot_ids:
            return
        
        if garden_plot_map[i][j] == symbol:
            plot_ids[i,j] = plot_id
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs(i+di, j+dj, symbol, plot_id)

new_area_id = 0
for row in range(len(garden_plot_map)):
    for col in range(len(garden_plot_map[0])):
        if (row, col) not in plot_ids:
            dfs(row, col, garden_plot_map[row][col], new_area_id)
            new_area_id += 1

plot_points = {}
for point, plot_id in plot_ids.items():
    plot_points.setdefault(plot_id, set()).add(point)

print(len(plot_points))

total_price = 0
for plot_id, points in plot_points.items():
    area = len(points)
    perimeter_points = set()
    for row, col in points:
        for drow, dcol in [(1,0), (0,1), (-1,0), (0,-1)]:
            nrow, ncol = row+drow, col+dcol
            if nrow not in range(len(garden_plot_map)) or ncol not in range(len(garden_plot_map[0])) or (nrow, ncol) not in points:
                perimeter_points.add(((row, col), (nrow, ncol)))
    
    total_price += area * len(perimeter_points)

print("Total price:", total_price)