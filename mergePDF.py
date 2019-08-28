import PyPDF2 
  
def PDFmerge(pdfs, output):  
    # creating pdf file merger object 
    pdfMerger = PyPDF2.PdfFileMerger() 
      
    # appending pdfs one by one 
    for pdf in pdfs: 
        with open(pdf, 'rb') as f: 
            pdfMerger.append(f) 
          
    # writing combined pdf to output pdf file 
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 
  
def main(): 
    # pdf files to merge 
    pdfs = ['(Cho and Yoon, 2015).pdf','(Dewanjee et al., 2017).pdf', '(Hussain et al., 2016).pdf','(Li et al., 2016).pdf', 
             '(Ondieki et al., 2017).pdf', '(Roth et al., 2011a).pdf','(Roth et al., 2011b).pdf','(Wang and Sweet, 2012).pdf',
             '(Yoshida et al., 2006).pdf','(Zha, 2018).pdf','10.1002@bmc.3721.pdf','10.1016@j.cbi.2019.01.030.pdf','10.1016@j.eplepsyres.2019.03.012.pdf',
             '228_2011_Article_1174.pdf','453.full.pdf','1472-6882-13-199.pdf','1519_5.pdf','19126-48332-1-PB.pdf','A Three-dimensional Model of Human Organic Anion.pdf',
             'Anti-Hyperglycemic and Renal Protective Activities.pdf','brewer2017.pdf',
             'chen2014.pdf','dmd.115.065987.pdf','Drug Metab Dispos-2003-Pang-1507-19.pdf','Drug Metab Dispos-2008-Polli-695-701.pdf',
           'dti-7-2013-027.pdf', 'Flavonoid conjugates interact with organic anion transporters (OATs) and.pdf','fphar-05-00178.pdf','huang2018.pdf','ijcem0008-15549.pdf',
           'Impact of curcumin on the pharmacokinetics.pdf','Induction of Andrographolide, A Biologically Active.pdf','Interaction and transport characteristics of mycophenolic.pdf',
           'iwanaga2012.pdf','ji2017.pdf','jing2015.pdf','jing2016.pdf','kibathi2018.pdf', 'Lee et al., 2010-In vitro inhibitory effects of Wen-pi-tang-Hab-Wu-ling-san on Human Cytochrome P450 isoforms.pdf','li2016.pdf',
            'li2018.pdf','Liang et al 2015.pdf','liu2015.pdf',
            'loss of drug in GI.pdf','main.pdf','molecules-19-05748.pdf',
            'molecules-20-00792.pdf','Nephroprotective activities of root extracts of Andrographis.pdf','nihms624114.pdf',
            'rehman2016.pdf','Renal Drug Transporters and Drug Interactions.pdf','Renoprotective effects of Andrograhis paniculate (Burm. f.) Nees inrats.pdf',
            'russo2013.pdf','Simple HPLC-UV method for determination.pdf','tang2016.pdf',
            'Terada et al 2015.pdf','The anthraquinone drug rhein potently interferes with organic anion.pdf','ting2017.pdf',
            'tr-32-207.pdf','Validation of a Total IC50 Method Which Enables In.pdf','Walsky and Obach, 2004-Validated assay for human cytochrome P450 activities (2).pdf',
            'wu2015.pdf','zac4153.pdf','zhang2017.pdf']
    # output pdf file name 
    output  = 'combined_example.pdf'
      
    # calling pdf merge function 
    PDFmerge(pdfs = pdfs, output = output) 
  
if __name__ == "__main__": 
    # calling the main function 
    main() 