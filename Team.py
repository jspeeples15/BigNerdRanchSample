# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:24:53 2017

@author: Jack
"""


"""
Team Stats include:
Offense:
Points per game 0
Yards per game 1
rushing yards per game 2
passing yards per game 3

Defense:
Points per game 4 
Yards per game 5
rushing yards per game 6
passing yards per game 7 

Special Teams:
Avg Kickoff (kicking) 8
Avg Kickoff (receiving) 9
Avg Punting (kicking) 10
Avg Punting (receiving) 11
Field Goal Percentage 12     

"""
class Team:
    name= "default"
    confrence = "default"
    wins = 0
    losses = 0
    confWins = 0
    confLosses = 0
    rankingFactor = 0.0
    
    #stats
    oppg = 0
    oypg = 0
    orypg = 0
    opypg = 0
    
    dppg = 0
    dypg = 0
    drypg = 0
    dpypg = 0
    
    stkor = 0
    stpk = 0
    stpr = 0
    stfgp = 0
        
    def __init__(self, newName="default", conf="default", stats=[0,0,0,0,0,0,0,0,0,0,0,0]):
        self.name = newName
        self.confrence = conf
        self.oppg = stats[0] 
        self.oypg = stats[1] 
        self.orypg = stats[2] 
        self.opypg = stats[3] 
        
        self.dppg = stats[4] 
        self.dypg = stats[5] 
        self.drypg = stats[6] 
        self.dpypg = stats[7]  
        
        self.stkor = stats[8] 
        self.stpk = stats[9] 
        self.stpr = stats[10] 
        self.stfgp = stats[11] 
        
        
    def getName(self):
        return self.name
    
    def getRecord(self):
        return [self.wins,self.losses]
    
    def getConfrenceRecord(self):
        return [self.confWins,self.confLosses]
    
    def getRankScore(self):
        return self.rankingFactor
    
    def addWin(self):
        self.wins = self.wins + 1
        
    def addLose(self):
        self.losses = self.losses + 1
    
    def addConfrenceWin(self):
        self.confWins = self.confWins + 1
        
    def addConfrenceLoss(self):
        self.confLosses = self.confLosses + 1
        
    def modifyStats(self, quality):
        gamesPlayed = self.wins + self.losses
        
        self.oppg = ((self.oppg * gamesPlayed) + (self.oppg*quality)) / (gamesPlayed + 1)
        self.oypg = ((self.oypg * gamesPlayed) + (self.oypg*quality)) / (gamesPlayed + 1) 
        self.orypg = ((self.orypg * gamesPlayed) + (self.orypg*quality)) / (gamesPlayed + 1) 
        self.opypg = ((self.opypg * gamesPlayed) + (self.opypg*quality)) / (gamesPlayed + 1) 
        
        self.dppg = ((self.dppg * gamesPlayed) + (self.dppg*quality)) / (gamesPlayed + 1) 
        self.dypg = ((self.dypg * gamesPlayed) + (self.dypg*quality)) / (gamesPlayed + 1) 
        self.drypg = ((self.drypg * gamesPlayed) + (self.drypg*quality)) / (gamesPlayed + 1) 
        self.dpypg = ((self.dpypg * gamesPlayed) + (self.dpypg*quality)) / (gamesPlayed + 1)  
        
        self.stkor = ((self.stkor * gamesPlayed) + (self.stkor*quality)) / (gamesPlayed + 1) 
        self.stpk = ((self.stpk * gamesPlayed) + (self.stpk*quality)) / (gamesPlayed + 1) 
        self.stpr = ((self.stpr * gamesPlayed) + (self.stpr*quality)) / (gamesPlayed + 1) 
        self.stfgp = ((self.stfgp * gamesPlayed) + (self.stfgp*quality)) / (gamesPlayed + 1) 
   
    def scoreTeam(self, stats):
        score = 0.0
        
        avgoppg = stats[0] #got
        avgoypg = stats[1] #got
        avgorypg = stats[2] #got
        avgopypg = stats[3] #got
        
        avgdppg = stats[4] #got
        avgdypg = stats[5] #got
        avgdrypg = stats[6] #got
        avgdpypg = stats[7] #got 
        
        avgstkor = stats[8] #got
        avgstpk = stats[9] #got
        avgstpr = stats[10] #got
        avgstfgp = stats[11] #got
        

        diffOppg = self.oppg - avgoppg
        diffOypg = self.oypg - avgoypg
        diffOrypg = self.orypg - avgorypg
        diffOpypg = self.opypg - avgopypg
        
        diffDppg = avgdppg - self.dppg
        diffDypg = avgdypg - self.dypg
        diffDrypg = avgdrypg - self.drypg
        diffDpypg = avgdpypg - self.dpypg
        
        diffStkor = self.stkor - avgstkor
        diffStpk = self.stpk - avgstpk
        diffStpr = self.stpr - avgstpr
        diffStfgp = self.stfgp - avgstfgp
        
        score += (diffOppg / 2.0)
        score += (diffOypg / 10.0)
        score += (diffOrypg / 12.0)
        score += (diffOpypg / 7.0)
        
        score += (diffDppg / 2.0)
        score += (diffDypg / 10.0)
        score += (diffDrypg / 12.0)
        score += (diffDpypg / 7.0)
        
        score += (diffStkor / 2.0)
        score += (diffStpk / 5.0)
        score += (diffStpr / 6.0)
        score += (diffStfgp / 5.0)
        
        score += (self.wins * 10.0)
        score += (self.losses * -20.0)
        
        self.rankingFactor = score