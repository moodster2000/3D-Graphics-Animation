# Object Modeling for Dugtrio
from __future__ import division

time = 0   # time is used to move objects from one frame to another
changePlatform = 0
ballDrop = 0
ballExpand = 0
rockmoving = 0
def setup():
    size (800, 800, P3D)
    frameRate(120)       # this seems to be needed to make sure the scene draws properly
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view

def draw():
    
    global time, changePlatform, ballDrop, ballExpand, rockmoving
    time += 0.01
    
    # camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
    if(0<time<4):
        camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera of the entire platform 
    elif(4 <= time < 5) :
        camera (-15+time*2, -10, 0, 45+time, 0, 0, 0, 1, 0) # position of the jiggly 
    elif (5 <= time < 6): 
        camera (10-time, -10, -0, -40-time, 0, 0, 0, 1, 0)  # position of the diglett 
    elif(6 <= time < 8) :
        camera (-15+time*2, -10, 0, 45+time, 0, 0, 0, 1, 0)  # position of the jiggly
    elif (8 <= time < 10): 
        camera (20-time, -10, -0, -45-time, 0, 0, 0, 1, 0)  # position of the diglett  
    elif (10 <= time < 10.5): 
        camera (-25+time*2, -10, 0, 45+time, 0, 0, 0, 1, 0)  # position of the jiggly
    elif (10.5 <= time < 12): 
        camera (20-time, -10, -0, -45-time, 0, 0, 0, 1, 0)  # position of the diglett
    elif (12 <= time < 15):
        camera (0, 0, 100-time*2, 0, 0, 0, 0,  1, 0) # position of the virtual camera of the entire platform   
    elif(time > 17):
        camera (10, -10, -0, -40, 0, 0, 0, 1, 0)  # position of the diglett
        
        fill(0, 102, 153)
        textAlign(CENTER)
        text("Winner:\nDugtrio", 0, 0)   

    background (200, 200, 255)  # clear screen and set background to light blue
    
    # set up the lights
    ambientLight(50, 50, 50)
    #use it for jiggly puff for funnies
    # pointLight(30, 30, 30, 35, 40, 36)
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    
    # set some of the surface properties
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    fill(255,255,0)
    #first
    pushMatrix()
    
    # #changeView
    if(time < 4):
        changePlatform = -time/15
        rotateX(changePlatform)
    
    if(12 < time <= 17):
        rotateX(-0.5) #platform view for rockblast
    
    #platform
    pushMatrix()
    translate (0, 0, 0)  # move up and dow
    rotateX(1.5708)
    scale (15, 10, 1)
    box(5)
    popMatrix()
    
    if(time < 2):
        ballDrop = time*30
        pushMatrix()
        scale(0.4,0.4,0.4)
        drawPokeball(-60,-80 + ballDrop,0)
        drawPokeball(60,-80 + ballDrop,0)
        popMatrix()
    if (2 <= time < 3):
        ballExpand = (time - 2)* 3  
        #pokeball opening
        fill(255,255,255)
        pushMatrix()
        translate(-24,-8,0)
        sphereDetail(50)  # this controls how many polygons make up each sphere
        sphere(2+ballExpand)
        popMatrix()
        
        #pokeball opening
        fill(255,255,255)
        pushMatrix()
        translate(24,-8,0)
        sphereDetail(50)  # this controls how many polygons make up each sphere
        sphere(2+ballExpand)
        popMatrix()
    if (3 <= time):
        #create dugtrio stage 1
        #dugtrio
        pushMatrix()
        translate(-20,-7.2,0)
        scale(0.4,0.4,0.4)
        rotateY(1.54)
        drawDugtrio()
        popMatrix()
        
        if(rockmoving <= 20):
            #jigglypuff
            pushMatrix()
            translate(20,-10,0)
            scale(0.4,0.4,0.4)
            rotateY(-1.54)
            drawJigglyPuff()
            popMatrix()
    
    if(time > 12 and rockmoving <= 20):
        rockmoving = (time-12) * 5
        #rockblast
        pushMatrix()
        translate(-22+rockmoving,-7.2,-5)
        rotateX(time)
        drawRockBlast()
        popMatrix()
        
        pushMatrix()
        translate(-20+rockmoving,-7.2,0)
        rotateX(time)
        drawRockBlast()
        popMatrix()
        
        pushMatrix()
        translate(-22+rockmoving,-7.2,5)
        rotateX(time)
        drawRockBlast()
        popMatrix()
    
    #final
    popMatrix()
    
    
   
    
    
    
def drawRockBlast():
    fill (245,222,179)
    pushMatrix()
    translate(10,-3,0)
    
    pushMatrix()
    translate (0, -3, 0)
    rotateZ(0)
    scale (1.5, 1.5, 1.5)
    cone(50)
    popMatrix()
    
    pushMatrix()
    translate (0, 3, 0)
    rotateZ(3.1451)
    scale (1.5, 1.5, 1.5)
    cone(50)
    popMatrix()
    
    pushMatrix()
    translate (0, 0, 3)
    rotateX(-1.54)
    scale (1.5, 1.5, 1.5)
    cone(50)
    popMatrix()
    
    pushMatrix()
    translate (0, 0, -3)
    rotateX(1.54)
    scale (1.5, 1.5, 1.5)
    cone(50)
    popMatrix()
    
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.3, 0.3, 0.3)
    sphere(10)
    popMatrix()

def drawDugtrio():
    global time
    goingUP = 33
    drawDiglett1(0,0,0)
    if(8 <= time < 10):    
        pushMatrix()
        rotateZ (0.0872665)
        drawDiglett2(19,33-(time*3),5) #full up value
        popMatrix()
        pushMatrix()
        rotateZ (-0.0872665)
        drawDiglett3(-19.5,33-(time*3.5),-5)
        popMatrix()
    if(time >= 10):
        pushMatrix()
        rotateZ (0.0872665)
        drawDiglett2(19,-2.5,5)
        popMatrix()
        pushMatrix()
        rotateZ (-0.0872665)
        drawDiglett3(-19.5,-7.5,-5)
        popMatrix()

def drawPokeball(x,y,z):
    
    fill (0,0,0)
    pushMatrix()
    translate (x, y,z)
    rotateX(1.5708)
    scale (4, 4, 1.5)
    torus()
    popMatrix()
    
    # a mainbody sphere
    fill (255,0,0)
    pushMatrix()
    translate (x, y, z)  # move up and down
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(5)
    popMatrix()
    

def drawJigglyPuff():
    global time
    if(time > 5):
        #eyebrow left
        fill (0, 0, 0)
        pushMatrix()
        translate (-5, -8, 14)  # move up and down
        rotateZ(0.523599)
        scale (1, 0.2, 0.2)
        box(5)
        popMatrix()
        
        #eyebrow right
        fill (0, 0, 0)
        pushMatrix()
        translate (5, -8, 14)  # move up and down
        rotateZ(-0.523599)
        scale (1, 0.2, 0.2)
        box(5)
        popMatrix()
    
    
    #mouth
    fill (0, 0, 0)
    pushMatrix()
    translate (0, 4, 14.5)  # move up and down
    # scale (1, 1, 0.2)
    if (3< time < 12.5):
        scale (1+1*(time/2.5), 1+0.1*(time/1.5), 0.2)
    cylinder()
    popMatrix()
    
    #eye left
    fill (255, 255, 255)
    pushMatrix()
    translate (5, -3, 14)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.3, 0.3, 0.1)
    sphere(10)
    popMatrix()
    
    #pupil right
    fill (0, 255, 0)
    pushMatrix()
    translate (5, -3, 14)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.15, 0.15, 0.15)
    sphere(10)
    popMatrix()
    
    #eye left
    fill (255, 255, 255)
    pushMatrix()
    translate (-5, -3, 14)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.3, 0.3, 0.1)
    sphere(10)
    popMatrix()
    
    #pupil right
    fill (0, 255, 0)
    pushMatrix()
    translate (-5, -3, 14)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.15, 0.15, 0.15)
    sphere(10)
    popMatrix()
    
    #little bump on head, sphere
    fill (255,20,147)
    pushMatrix()
    translate (-3, -10, 10)  # move up and down
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(3.5)
    popMatrix()
    
    #ears cones left
    fill (255,20,147)
    pushMatrix()
    rotateZ(-0.6)
    translate (-3, -16, 5)
    scale (5, 5, 5)
    cone(50)
    popMatrix()
    
    #ears cones right
    fill (255,20,147)
    pushMatrix()
    rotateZ(0.6)
    translate (3, -16, 5)
    scale (5, 5, 5)
    cone(50)
    popMatrix()
    
    # a mainbody sphere
    fill (255,20,147)
    pushMatrix()
    translate (0, 0, 0)  # move up and down
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(15)
    popMatrix()
    
    # #arm left
    fill (255,20,147)
    pushMatrix()
    rotateZ(1.5708)
    rotateY(1.5708)
    translate (0, 17, 0)  # move mup and down
    scale(2,0.5,0.5)
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(5)
    popMatrix()
    
    # #arm right
    fill (255,20,147)
    pushMatrix()
    rotateZ(1.5708)
    rotateY(1.5708)
    translate (0, -17, 0)  # move up and down
    scale(2,0.5,0.5)
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(5)
    popMatrix()
    
    #foot left
    fill (255,20,147)
    pushMatrix()
    rotateY(1.5708)
    translate (0, 15, -5)  # move up and down
    scale(2,0.5,0.5)
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(5)
    popMatrix()
    
    #foot left
    fill (255,20,147)
    pushMatrix()
    rotateY(1.5708)
    translate (0, 15, 5)  # move up and down
    scale(2,0.5,0.5)
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(5)
    popMatrix()


def drawDiglett1(x,y,z):
    
    #litte hair sprouts
    fill (255,255,102)
    pushMatrix()
    translate (0+x, -22+y, z)
    rotateX(1.5708)
    scale (0.5, 0.5, 3)
    cylinder()
    popMatrix()
    
    fill (255,255,102)
    pushMatrix()
    translate (1+x, -22+y, z)
    rotateX(1.5708)
    rotateY(0.5)
    scale (0.5, 0.5, 2)
    cylinder()
    popMatrix()
    
    fill (255,255,102)
    pushMatrix()
    translate (-1+x, -22+y, z)
    rotateX(1.5708)
    rotateY(-0.5)
    scale (0.5, 0.5, 2)
    cylinder()
    popMatrix()
    
    
    # nose
    fill (255, 0, 0)
    pushMatrix()
    translate (0+x, -4+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.5, 0.2, 0.2)
    sphere(10)
    popMatrix()

    #eye
    fill (0, 0, 0)
    pushMatrix()
    translate (3+x, -10+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.1, 0.2, 0.1)
    sphere(10)
    popMatrix()
    
    #eye
    fill (0, 0, 0)
    pushMatrix()
    translate (-3+x, -10+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.1, 0.2, 0.1)
    sphere(10)
    popMatrix()
    
    # head
    fill (181, 101, 29)
    pushMatrix()
    translate (0+x, -10+y, 0+z)  # move up and down
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(10)
    popMatrix()

    # a mainbody cylinder
    fill (181, 101, 29)
    pushMatrix()
    translate (0+x, 0+y, 0+z)
    rotateX(1.5708)
    scale (10, 10, 10)
    cylinder()
    popMatrix()
    
    #hole in the ground effect/torus shape
    fill (102,102,0)
    pushMatrix()
    translate (0+x, 10+y, 0+z)
    rotateX(1.5708)
    scale (10, 10, 4)
    torus()
    popMatrix()

def drawDiglett2(x,y,z):
    
    #eyebrow
    fill (0, 0, 0)
    pushMatrix()
    translate (-3+x, -12.5+y, 9.5+z)  # move up and down
    rotateZ(0.523599)
    scale (1, 0.2, 0.2)
    box(5)
    popMatrix()
    
    #eyebrow
    fill (0, 0, 0)
    pushMatrix()
    translate (3+x, -12.5+y, 9.5+z)  # move up and down
    rotateZ(-0.523599)
    scale (1, 0.2, 0.2)
    box(5)
    popMatrix()
    
    
    # nose
    fill (255, 0, 0)
    pushMatrix()
    translate (0+x, -2+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.4, 0.4, 0.2)
    sphere(10)
    popMatrix()

    #eye
    fill (0, 0, 0)
    pushMatrix()
    translate (3+x, -10+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.1, 0.1, 0.1)
    sphere(10)
    popMatrix()
    
    #eye
    fill (0, 0, 0)
    pushMatrix()
    translate (-3+x, -10+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.1, 0.1, 0.1)
    sphere(10)
    popMatrix()
    
    # head
    fill (181, 101, 29)
    pushMatrix()
    translate (0+x, -13+y, 0+z)  # move up and down
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(10)
    popMatrix()

    # a mainbody cylinder
    fill (181, 101, 29)
    pushMatrix()
    translate (0+x, 0+y, 0+z)
    rotateX(1.5708)
    scale (10, 10, 13)
    cylinder()
    popMatrix()
    
    #hole in the ground effect/torus
    fill (102,102,0)
    pushMatrix()
    translate (0+x, 13+y, 0+z)
    rotateX(1.5708)
    scale (10, 10, 3)
    torus()
    popMatrix()
    
def drawDiglett3(x,y,z):
    
    #eyebrow
    fill (128,128,0)
    pushMatrix()
    translate (-3+x, -12.5+y, 9.5+z)  # move up and down
    rotateZ(0)
    scale (1, 0.2, 0.2)
    box(5)
    popMatrix()
    
    #eyebrow
    fill (128,128,0)
    pushMatrix()
    translate (3+x, -12.5+y, 9.5+z)  # move up and down
    rotateZ(0)
    scale (1, 0.2, 0.2)
    box(5)
    popMatrix()
    
    
    # nose
    fill (255,218,185)
    pushMatrix()
    translate (0+x, -1+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.4, 0.6, 0.2)
    sphere(10)
    popMatrix()

    #eye
    fill (0, 0, 0)
    pushMatrix()
    translate (3+x, -10+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.2, 0.1, 0.1)
    sphere(10)
    popMatrix()
    
    #eye
    fill (0, 0, 0)
    pushMatrix()
    translate (-3+x, -10+y, 9.5+z)  # move up and down
    sphereDetail(10)  # this controls how many polygons make up each sphere
    scale (0.2, 0.1, 0.1)
    sphere(10)
    popMatrix()
    
    # head
    fill (181, 101, 29)
    pushMatrix()
    translate (0+x, -18+y, 0+z)  # move up and down
    sphereDetail(50)  # this controls how many polygons make up each sphere
    sphere(10)
    popMatrix()

    # a mainbody cylinder
    fill (181, 101, 29)
    pushMatrix()
    translate (0+x, 0+y, 0+z)
    rotateX(1.5708)
    scale (10, 10, 18)
    cylinder()
    popMatrix()
    
    #hole in the ground effect/torus
    fill (102,102,0)
    pushMatrix()
    translate (0+x, 17+y, 0+z)
    rotateX(1.5708)
    scale (10, 10, 3)
    torus()
    popMatrix()


# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
        
def torus(radius=1.0, tube_radius=0.5, detail_x=16, detail_y=16):
    radius = float(radius)
    tube_radius = float(tube_radius)
    detail_x = int(detail_x)
    detail_y = int(detail_y)

    tube_ratio = (tube_radius / radius)

    def make_torus():
        vertices = []
        normals = []
        for torus_segment in range(detail_x):
            theta = 2 * PI * torus_segment / detail_x
            cos_theta = cos(theta)
            sin_theta = sin(theta)

            segment_vertices = []
            segment_normals = []

            for tube_segment in range(detail_y):
                phi = 2 * PI * tube_segment / detail_y
                cos_phi = cos(phi)
                sin_phi = sin(phi)
                segment_vertices.append(PVector(
                    cos_theta * (radius + cos_phi * tube_radius),
                    sin_theta * (radius + cos_phi * tube_radius),
                    sin_phi * tube_radius,
                ))
                segment_normals.append(PVector(
                    cos_phi * cos_theta,
                    cos_phi * sin_theta,
                    sin_phi,
                ))
            vertices.append(segment_vertices)
            normals.append(segment_normals)
        return vertices, normals

    global GEOMETRY_CACHE
    try:
        GEOMETRY_CACHE
    except NameError:
        GEOMETRY_CACHE = {}
    cache_index = ("torus", radius, tube_radius, detail_x, detail_y)
    if cache_index in GEOMETRY_CACHE:
        vertices, normals = GEOMETRY_CACHE[cache_index]

    else:
        vertices, normals = make_torus()
        GEOMETRY_CACHE[cache_index] = (vertices, normals)

    for i in range(detail_x):
        for j in range(detail_y):
            beginShape()

            normal(normals[i][j].x, normals[i][j].y, normals[i][j].z)
            vertex(vertices[i][j].x, vertices[i][j].y, vertices[i][j].z)
            normal(normals[(i + 1) % detail_x][j].x, normals[(i + 1) % detail_x][j].y, normals[(i + 1) % detail_x][j].z)
            vertex(vertices[(i + 1) % detail_x][j].x, vertices[(i + 1) % detail_x][j].y, vertices[(i + 1) % detail_x][j].z)
            normal(normals[(i + 1) % detail_x][(j + 1) % detail_y].x, normals[(i + 1) % detail_x][(j + 1) % detail_y].y, normals[(i + 1) % detail_x][(j + 1) % detail_y].z)
            vertex(vertices[(i + 1) % detail_x][(j + 1) % detail_y].x, vertices[(i + 1) % detail_x][(j + 1) % detail_y].y, vertices[(i + 1) % detail_x][(j + 1) % detail_y].z)
            normal(normals[i][(j + 1) % detail_y].x, normals[i][(j + 1) % detail_y].y, normals[i][(j + 1) % detail_y].z)
            vertex(vertices[i][(j + 1) % detail_y].x, vertices[i][(j + 1) % detail_y].y, vertices[i][(j + 1) % detail_y].z)

            endShape(CLOSE)
            
# Draw a cone pointing in the -y direction (up), with radius 1, with y in range [-1, 1]
def cone(sides=50):
    sides = int(sides)

    # draw triangles making up the sides of the cone
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        theta_next = 2.0 * PI * (i + 1) / sides
        
        beginShape()
        normal(cos(theta), 0.6, sin(theta))
        vertex(cos(theta), 1.0, sin(theta))
        normal(cos(theta_next), 0.6, sin(theta_next))
        vertex(cos(theta_next), 1.0, sin(theta_next))
        normal(0.0, -1.0, 0.0)
        vertex(0.0, -1.0, 0.0)
        endShape()

    # draw the cap of the cone
    beginShape()
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        vertex(cos(theta), 1.0, sin(theta))
    endShape()
