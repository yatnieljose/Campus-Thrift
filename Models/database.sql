CREATE TABLE [Accounts] ( 
	[AccountId] INTEGER PRIMARY KEY, 
	[Name] NVARCHAR(50)  NOT NULL, 
    [Email] NVARCHAR(50)  NOT NULL,
    [Password] NVARCHAR(50) NOT NULL,
    [Bio] NVARCHAR(250)  NOT NULL,
    [ProfilePicture] BLOB,
    [Rank] INTEGER NOT NULL
); 
CREATE TABLE [Items] (  
	[ItemId] INTEGER  PRIMARY KEY NOT NULL,
	[SellerId] INTEGER NOT NULL,   
    [Name] NVARCHAR(50) NOT NULL,
    [TypeId] INTEGER NOT NULL,
    [MinimumBid] INTEGER NOT NULL,
    [HighestBid] INTEGER,
    [BuyerId] INTEGER
);     
CREATE TABLE [Receipts] (  
    [ReceiptId] INTEGER NOT NULL PRIMARY KEY,
	[ItemId] INTEGER  NOT NULL,  
	[BuyerId] INTEGER NOT NULL
); 

CREATE TABLE [Types] (
    [TypeId] INTEGER NOT NULL PRIMARY KEY,
    [Name] NVARCHAR(50) NOT NULL
);