from registry.testing.setup import getAlgodClient

def registry_demo():
    client = getAlgodClient()
    print('did it')
    
if __name__=="__main__":
    registry_demo()