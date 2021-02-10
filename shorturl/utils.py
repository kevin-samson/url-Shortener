from shorturl.main import Reg


def ifExist(dat):
    query = Reg.query.filter_by(slug=dat).first()
    if query is not None:
        return True
    else:
        return False
