from django.db import models

Brands = (
        (0,'Unknown'),
        (1,'Herman Miller'),
        (2,'Steelcase'),
        (3,'Teknion'),
        (4,'Haworth'),   
        (5,'Knoll'),
        (6,'Wilkhahn'),
        (7,'Benel'),
        (8,'Fusys'),
        (9,'Humanscale'),
        (10,'Enjoy'),
        (11,'Ergohuman'),
        (12,'Artmatrix'),
        
)

Warehouses = (
        (1,'E9 Premium, #06-17'),
        (2,'Hiangkie Industrial Building, #04-14'),
        (3,'Mayfair Industrial Building, #05-30'),   
)
Area_Codes = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10'),
    (11,'11'),
    (12,'12'),
    (13,'13'),
    (14,'14'),
    (15,'15'),
    (16,'16'),
    (17,'17'),
    (18,'18'),
    (19,'19'),
    (20,'20'),
    (21,'21'),
    (22,'22'),
    (23,'23'),
    (24,'24'),
    (25,'25'),
    (26,'26'),
    (27,'27'),
    (28,'28'),
    (29,'29'), 
    (30,'30'),
    (31,'31'),
    (32,'32'),
    (33,'33'),
    (34,'34'),
    (35,'35'),
    (36,'36'),
    (37,'37'),  
    (38,'38'),
    (39,'39'),
    (40,'40'),
    
)
# Create your models here.
class Desk(models.Model):
    class Meta:
        db_table = 'Desks'

    Hole_Types = (
        (1,'Rectangular'),  #including square
        (2,'Round'),
        (3,'Flat'),  # No hole
        (4,'Others'),
        (5,'Half Round'), #月牙
    )
    Table_Top_Colors = (
        (1,'Maple'),
        (2,'White'),
        (3,'Grey'),
        (4,'Cherry'),   
        (5,'Brown'),
        (6,'Beech'),
        (7,'Ivory'),
        (8,'Black'),
    
    )

    Length_Options = (
        (400,'400'),
        (450,'450'),
        (500,'500'),
        (600,'600'),
        (650,'650'),
        (700,'700'),
        (750,'750'),
        (800,'800'),
        (850,'850'),
        (900,'900'),
        (1100,'1100'),
        (1200,'1200'),
        (1350,'1350'),
        (1400,'1400'),
        (1450,'1450'),       
        (1500,'1500'),
        (1600,'1600'),
        (1650,'1650'),
        (1700,'1700'),
        (1800,'1800'),
        (2100,'2100'),       
        (-1,'Other Measurements'),
        
    )

    Hole_Positions = (
        (1,'Front Middle'),
        (2,'Two Ends'),
        (3,'Left End'),  
        (4,'Corner'),
        (5,'Right End'),        
    )

    Table_Shapes = (
        (0,'L Shape Desk - Left Sided'),
        (1,'L Shape Desk - Right Sided'),
        (2,'Straight'),
        (3,'P Shape'),   
        (4,'B Shape'),
        (5,'Square'),
        (6,'Oval'),
        (7,'Boat Shape'),
        (8,'Other'),
        (9,'L Shape - Left OR Right'),
    )

    Thickness_Options = (
        (1,'25mm'),
        (2,'30mm'),
        (3,'Less than 25mm'),  
        (4,'Others'),       
    )

    Holes_Qty = (
        (0,'0'),
        (1,"1"),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    )

    #仓库号
    Warehouse_Code = models.IntegerField(
        choices=Warehouses,
        default=0
    )

    #区号
    Area_Code = models.IntegerField(choices=Area_Codes,default=1)

    #照片
    Image = models.CharField(
        max_length = 200,
        default="",
        blank=True
    )
    #牌子
    Brand = models.IntegerField(
        choices=Brands,
        default=0
    )

    #Table Top Color
    Table_Top_Color = models.IntegerField(choices=Table_Top_Colors,default=1)
    
    #Table Shape
    Table_Shape = models.IntegerField(choices=Table_Shapes,default=3)
    
    # Measurements
    Length = models.IntegerField(choices=Length_Options,default=1500)
    Odd_Length = models.IntegerField(blank=True,null=True)
    Width = models.IntegerField(choices=Length_Options,default=600)
    Odd_Width = models.IntegerField(blank=True,null=True)
    Thickness = models.IntegerField(choices=Thickness_Options,default=1)
    Thickness_Details = models.IntegerField(blank=True,null=True)
    
    Main_Depth = models.IntegerField(choices=Length_Options,default=600)
    Odd_Main_Depth = models.IntegerField(blank=True,null=True)
    Side_Depth = models.IntegerField(choices=Length_Options,default=600)
    Odd_Side_Depth = models.IntegerField(blank=True,null=True)
    Hole_Quantity = models.IntegerField(choices=Holes_Qty,default=1)
    Hole_Shape = models.IntegerField(choices=Hole_Types,default=2)
    Hole_Position = models.CharField(
        max_length = 200,
        blank=True,
        default=""
    )

    #是否有问题
    Is_Faulty = models.BooleanField(default=False)
    Description = models.TextField(
        max_length = 500,
        blank=True,
        default=""
    )
    #Qty
    Quantity_For_This_Entry = models.IntegerField(
        
    )

    #Custom Code
    Custom_Code = models.CharField(
        max_length = 20,
        default=""
    )
