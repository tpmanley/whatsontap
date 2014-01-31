from whatsontap import db, Tap, app


with app.app_context():
    session = db.session()
    db.metadata.create_all(db.engine)
    session.merge(Tap(id=1,
                    name="Short Circuit Stout",
                    style="sweet stout",
                    abv="5.4%",
                    description="""Short Circuit Stout is a full-bodied and roasty stout with a lingering sweet aftertaste.
It uses 5 different malts to create a variety of flavors that change through the course of taking a sip.""",
                    image="/images/short-circuit-stout.jpg"))
    session.merge(Tap(id=2,
                    name="Flip Switch IPA",
                    style="American IPA",
                    abv="6.1%",
                    description="""Flip Switch IPA is a hoppy American pale ale with a slight citrus aroma. It features
a variety of American hops, with just the right amount of bitterness to match the malty base.""",
                    image="http://placekitten.com/200/200"))
    session.merge(Tap(id=3,
                      name="Wheatstone Bridge",
                      style="American style wheat",
                      abv="6.3%",
                      description="""Wheatstone Bridge is a light and refreshing wheat beer with distinct flavors of
honey and chamomile tea. Made by adding Minnesota honey to an American malted wheat base, the final step involves
steeping chamomile tea.""",
                      image="http://placekitten.com/200/200"))
    session.commit()