import P4

def test_Cluster():
    P3_output = [[0.0, 0.4522470626742357, 0.4522470626742357, 0.3641308618362756, 0.3641308618362756, 0.30409883108112323, 0.31925086156926286],
                 [0.4522470626742357, 0.0, 0.36811871779449096, 0.3802009262047681, 0.4197118409515671, 0.4408399986765892, 0.30409883108112323],
                 [0.4522470626742357, 0.36811871779449096, 0.0, 0.36360138775851414, 0.5033762053808777, 0.28235817842618405, 0.31811793084023765],
                 [0.3641308618362756, 0.3802009262047681, 0.36360138775851414, 0.0, 0.35584348469633686, 0.30409883108112323, 0.2326161962278796],
                 [0.3641308618362756, 0.4197118409515671, 0.5033762053808777, 0.35584348469633686, 0.0, 0.22219936210737928, 0.2326161962278796],
                 [0.30409883108112323, 0.4408399986765892, 0.28235817842618405, 0.30409883108112323, 0.22219936210737928, 0.0, 0.14836930749743993],
                 [0.31925086156926286, 0.30409883108112323, 0.31811793084023765, 0.2326161962278796, 0.2326161962278796, 0.14836930749743993, 0.0]]
    P3_output_labels = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]
    P4_output = P4.Cluster(P3_output, P3_output_labels)
    P4_output_expected = '((Bovine, Gibbon), ((((Chimp, Human), Gorilla), Orangutan), Mouse))'

    assert P4_output == P4_output_expected
