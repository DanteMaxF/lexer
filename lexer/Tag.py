

class TagClass:
    def __init__(self):
        self.EOF = 65535
        self.PROGRAM = 256
        self.CONSTANT = 257
        self.VAR = 258
        self.BEGIN = 259
        self.END = 260
        self.INTEGER = 261
        self.REAL = 262
        self.BOOLEAN = 263
        self.STRING = 264
        self.ASSIGN = 265
        self.WRITELN = 266
        self.READLN = 267
        self.WHILE = 268
        self.DO = 269 
        self.REPEAT = 270
        self.UNTIL = 271
        self.FOR = 272
        self.TO = 273
        self.DOWNTO = 274
        self.IF = 275
        self.THEN = 276
        self.ELSE = 277
        self.NOT = 278
        self.EQ = 279
        self.NEQ	= 280
        self.GE = 281
        self.LE = 282
        self.FALSE = 283
        self.TRUE = 284
        self.DIV	= 285
        self.MOD = 286
        self.AND	= 287
        self.OR = 288
        self.MINUS = 289
        self.ID = 290
        self.CHARACTERSTRING = 291
        self.COMMENTS = 292
        self.ERROR = 9999


Tag = TagClass()

