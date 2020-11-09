import random
from neo4j import GraphDatabase, basic_auth
import anb as anx
import datetime
import math

# levelList = {
#     'Red' : 1,
#     'Blue' : 2,
#     'Green' : 2,
#     'Lime' : 3,
#     'Cucumber' : 3,
#     'Beige' : 3,
#     'Violet' : 3,
# }

chart = anx.Chart(IdReferenceLinking=False)
chart.add_StrengthCollection(anx.StrengthCollection([
    anx.Strength(DotStyle="DotStyleDashed", Name="Dashed", Id="Dashed"),
    anx.Strength(DotStyle="DotStyleSolid", Name="Solid", Id="Solid")
]))

class LevelProperties(object):
    def __init__(self, color, colorHex, levelNum, ypos):
        self.color = color
        self.colorHex = colorHex
        self.levelNum = levelNum
        self.ypos = ypos

class Relationship(object):
    def __init__(self, relationshipType, endNodeProperties, endNodeNeoId):
        self.relationshipType = relationshipType
        self.endNodeProperties = endNodeProperties
        self.endNodeNeoId = endNodeNeoId

class Tree(object):
    def __init__(self, properties, neoId):
        self.properties = properties
        self.neoId = neoId
        self.level = ''
        self.fruitList = []             # List of fruits on this tree
        self.relationshipList = []      # Full neo object that has a link to this Tree object
        self.numOfFruit = 0

#----------------------------------------------------------------------------------------------------------------------
levelList = []
tempLevel = LevelProperties(color='Red', colorHex=0x0000FF, levelNum=1, ypos=0)
levelList.append(tempLevel)
tempLevel = LevelProperties(color='Blue', colorHex=0xFF0000, levelNum=2, ypos=300)
levelList.append(tempLevel)
tempLevel = LevelProperties(color='Green', colorHex=0x00FF00, levelNum=2, ypos=300)
levelList.append(tempLevel)
tempLevel = LevelProperties(color='Lime', colorHex=0x63FF97, levelNum=3, ypos=600)
levelList.append(tempLevel)
tempLevel = LevelProperties(color='Cucumber', colorHex=0x85FF66, levelNum=3, ypos=600)
levelList.append(tempLevel)
tempLevel = LevelProperties(color='Beige', colorHex=0xFF8E42, levelNum=3, ypos=600)
levelList.append(tempLevel)
tempLevel = LevelProperties(color='Violet', colorHex=0xFF456A, levelNum=3, ypos=600)
levelList.append(tempLevel)

graph_url = "bolt://localhost:7687"
graph_username = "admin"
graph_password = "admin"

driver =GraphDatabase.driver(graph_url, auth=basic_auth(graph_username, graph_password))
session = driver.session()
data = session.run('''match p=()-[:CONNECTED|:HAS]->() return p''').graph()

treeList = []
fruitList = []
for item in data._nodes:
    node = data._nodes[item]
    itemType = str(node).split('frozenset({\'')[1].split('\'}) properties')[0]
    if itemType == 'tree':
        treeList.append(Tree(properties=node._properties, neoId=node.id))
        for item in data._relationships:
            relationship = data._relationships[item]
            if relationship.start_node._properties == node._properties:
                treeList[-1:][0].relationshipList.append(Relationship(relationshipType=relationship.type, endNodeProperties=relationship._end_node._properties, endNodeNeoId=relationship._end_node.id))
        numOfFruit = 0
        for item in treeList[-1:][0].relationshipList:
            if item.relationshipType == 'HAS':
                numOfFruit += 1
        treeList[-1:][0].numOfFruit = numOfFruit

for item in treeList:               # Give each tree its level properties
    name = item.properties['name']
    for color in levelList:
        if color.color in name:
            item.level = color

tempList = []                   # Attempt to sort the treeList .... this doesn't work too well
for item in treeList:
    if item not in tempList:
        tempList.append(item)
    for downOne in treeList:
        if item.level.levelNum -1 == downOne.level.levelNum:
            for rel in downOne.relationshipList:
                if rel.endNodeProperties == item.properties:
                    if downOne not in tempList:
                        tempList.append(downOne)

# Num of fruits will dictate the positional Y value for the box size. We'll take care of fixing that now.
rowCount = 1
loopCount = 1
previousLevel = 0
for item in treeList:
    for relationship in item.relationshipList:
        if int(loopCount % 5) == 0:
            for item2 in treeList:
                if item2.level.levelNum < item.level.levelNum:
                    item2.level.ypos -= 50
                #item.level.ypos += 300
            #previousLevel = item.level.ypos
        loopCount += 1

# Draw boxes
xDict = {1 : 0, 2 : 0, 3 : 0}
for item in treeList:
    boxX = 150
    boxY = 150
    boxPosY = item.level.ypos
    xPadding = 20
    xpos = xDict[item.level.levelNum]
    if item.numOfFruit >= 5:
        boxX = boxX * 4
    else:
        boxX = boxX * item.numOfFruit
    if item.numOfFruit >= 5:
        boxY = boxY * math.ceil(item.numOfFruit / 5)
    chart_item_collection = anx.ChartItemCollection()
    boxstyle =      anx.BoxStyle(BackColour=item.level.colorHex, EntityTypeReference=None, Filled=True, FillStyle="Solid", LineWidth=4, LineColour=None, Strength=None, StrengthReference=None, Type=None, gds_collector_=None)
    box =           anx.Box(Depth=0, Height=boxY, TextX=2, TextY=1, Width=boxX, BoxStyle=boxstyle)
    entity =        anx.Entity(EntityId=item.neoId, Identity=item.neoId, LabelIsIdentity=False, Box=box,)
    end =           anx.End(Entity=entity, Label=None, X=0, Y=boxPosY, Z=0) # -------------------------------------------------------- This controls the vertical position
    chart_item =    anx.ChartItem(Description=None, Id=None, Label=item.properties['name'], End=end, Entity=entity, XPosition=xpos)
    chart_item_collection.add_ChartItem(chart_item)
    chart.add_ChartItemCollection(chart_item_collection)

    relX = xpos + 75
    relY = item.level.ypos + 75
    rowCount = 1
    loopCount = 1
    for relationship in item.relationshipList:
        if relationship.relationshipType == 'HAS':
            #print(int(item.numOfFruit), int(item.numOfFruit % 5))
            if math.ceil(int(loopCount % 5)) == 0:
                print('Next Level')
                relX = xpos + 75
                relY = relY + 150
                rowCount += 1
            fruit = relationship
            chart_item_collection = anx.ChartItemCollection()
            circle =        anx.FrameStyle(Colour=0xFFFFFF, Visible=1, Margin=None)
            icon =          anx.Icon(IconStyle=anx.IconStyle(Type="Male", FrameStyle=circle))
            entity =        anx.Entity(Icon=icon, EntityId=fruit.endNodeNeoId, Identity=fruit.endNodeNeoId)
            end =           anx.End(X=relX, Y=relY, Entity=entity)
            chart_item =    anx.ChartItem(XPosition=relX, Label=fruit.endNodeProperties['name'], End=end, Description=None)
            chart_item_collection.add_ChartItem(chart_item)
            chart.add_ChartItemCollection(chart_item_collection)
            relX += 150
            #relY = item.level.ypos + 75
            loopCount += 1

    xDict[item.level.levelNum] += boxX + xPadding

# Draw links
for item in treeList:
    for relationship in item.relationshipList:
        if relationship.relationshipType == 'CONNECTED':
            chart_item_collection = anx.ChartItemCollection()
            link_style = anx.LinkStyle(StrengthReference=None, Type='Link', ArrowStyle='ArrowNone', LineColour=None, MlStyle="MultiplicitySingle")
            link = anx.Link(End1Id=item.neoId, End2Id=relationship.endNodeNeoId, LinkStyle=link_style)
            chart_item = anx.ChartItem(Label=relationship.relationshipType, Link=link, Description='Test')
            chart_item_collection.add_ChartItem(chart_item)
            chart.add_ChartItemCollection(chart_item_collection)

with open('aaaaaaaaaaa.anx', 'w') as output_file:
    chart.export(output_file, 0, pretty_print=True, namespacedef_=None)