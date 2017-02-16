import matplotlib.pyplot as plt
import numpy as np
import xlrd
from datetime import datetime
import math

class DataVisualization:
    
    def visualization(self, index_):
        positive = []
        negative = []
        neutral = []
        date = []
        
        font = {'family': 'sans-serif',
                'color':  'black',
                'weight': 'normal',
                'size': 11,
                'multialignment': 'center'
                }
        
        workbook = xlrd.open_workbook('results.xlsx', 'utf-8')
        worksheet = workbook.sheet_by_index(index_)
        for i in range(2, worksheet.nrows):
            datetime_object = datetime.strptime(worksheet.cell(i,0).value, "%Y-%m-%d")
            date.append(datetime_object.strftime('%b-%d'))
           
        for c in range(0, 10, 3):   
            posCount = 0
            negCount = 0
            neutCount = 0  
            total = 0
            avgpos = 0
            avgneg = 0
            devpos = 0
            devneg = 0
            fig = plt.figure()
            plt.gca().set_color_cycle(['green', 'red', 'gray']) 
            for i in range(2, worksheet.nrows):
                date.append(int(worksheet.cell(i,c+1).value))
                positive.append(int(worksheet.cell(i,c+1).value))
                negative.append(int(worksheet.cell(i,c+2).value))
                neutral.append(int(worksheet.cell(i,c+3).value))
            
            m = max(positive)
            if(m < max(negative)):
                m = max(negative)
            if(m < max(neutral)):
                m = max(neutral)
            
            x = np.array([0,1,2,3,4,5,6])
            plt.xticks(x, date)
            y = np.array(positive)
            plt.plot(x, y, '-o')
            
            y = np.array(negative)
            plt.plot(x, y, '-o')
            
            y = np.array(neutral)
            plt.plot(x, y, '-o')
            
            plt.legend(['Positive Tweets', 'Negative Tweets', 'Neutral Tweets'], loc='upper right', fontsize=10)
            
            
            fig.suptitle(worksheet.cell(0,c+1).value, fontsize=20, color='darkred')
            plt.ylabel('# of %s' % worksheet.cell(0,c+1).value )
            plt.xlabel('Date')
            
            for y in range(5, m+5, 5):    
                plt.plot(range(0,7), [y] * len(range(0, 7)), "--", lw=0.5, color="black", alpha=0.3) 
            
            for i in range(0, 7):
                posCount += positive[i]
                negCount += negative[i]
                neutCount += neutral[i]
            
            total = posCount + negCount + neutCount
            avgpos = float(posCount) / 7
            avgneg = float(negCount) / 7
            
            sump = 0
            sumn = 0
            for i in range(0, 7):
                sump += math.pow(positive[i] - avgpos, 2)
                sumn += math.pow(negative[i] - avgneg, 2)
            
            devpos = format(math.sqrt( sump / 6 ), '.2f')
            devneg = format(math.sqrt( sumn / 6 ), '.2f')
            avgpos = format(avgpos, '.2f')
            avgneg = format(avgneg, '.2f')
            txt = ('__Week %s - Summary__\n\nTotal Tweets: %s\nPositive: %s\nNegative: %s\nNeutral: %s\nAvg Pos: %s\nAvg Neg: %s\n'
                   'St. Deviation Pos: %s\nSt. Deviation Neg: %s\n'%
                    (index_ + 1, total, posCount, negCount, neutCount, avgpos, avgneg, devpos, devneg))
            
            plt.text(6.1, 1, txt, fontdict=font)
            plt.subplots_adjust(right=0.70)
            
            #plt.figure(figsize=(12, 14))
            plt.show()
            positive = []
            negative = []
            neutral = []
            
if __name__ == '__main__':
    dv = DataVisualization()
    dv.visualization(0)
    dv.visualization(1)
    
