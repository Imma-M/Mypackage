from Mypackage import myModule

def test_top_n():
    """
    Make sure top_n works correctly

    """
    assert myModule.top_n([8,2,3,4,7,6],3)==[8,7,6], 'incorrect'
    assert myModule.top_n([10,1,4,6,2,0],2)==[10,6], 'incorrect'
    assert myModule.top_n([1,3,2,6,5,8],4)==[8,6,5,3], 'incorrect'