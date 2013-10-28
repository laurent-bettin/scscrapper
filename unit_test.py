import scscrapper
import unittest
from bs4 import BeautifulSoup

class TestScScrapper(unittest.TestCase):

    def setUp(self):
        self.empty_bs_instance = BeautifulSoup('', 'html5lib')
        self.test_item = BeautifulSoup('''
        <li class="elco-collection-item">
            <figure data-sc-play-value="" data-sc-parameter-id="0" data-sc-play-type="videos" data-sc-product-id="497832" data-rel="btn-play-product sc-button " class="d-media small  elco-collection-left">
                <div class="d-media-videos"></div>
                <small class="d-media-caption videos"></small>
                <img width="120" height="163" alt="Affiche The Barber, l'homme qui n'était pas là" src="http://media.senscritique.com/media/000000108401/120/The_Barber_l_homme_qui_n_etait_pas_la.jpg" class="d-poster-1">
            </figure>
            <div class="elco-collection-content">
                <span class="elco-original-title">The Man Who Wasn't There</span>
                <h2 class="elco-title">
                    <a id="product-title-497832" class="elco-anchor" href="/film/The_Barber_l_homme_qui_n_etait_pas_la/497832">The Barber, l'homme qui n'était pas là</a>
                    <span class="elco-date">(2001)</span>
                </h2>
                <p class="elco-baseline">Film de
                    <a class="elco-baseline-a" href="/contact/Joel_Coen/7566">Joel Coen</a> et <a class="elco-baseline-a" href="/contact/Ethan_Coen/8736">Ethan Coen</a>
                </p>
                <p class="elco-description">Durant l'été 1949, dans une petite ville du nord de la Californie, Ed Crane soupçonne sa femme Doris de le tromper avec son patron. Un jour, il fait la...</p>
                <div class="erra ">
                    <div class="erra-main">
                        <div class="erra-ratings">
                            <a title="" data-sc-tooltip="true" class="erra-global" href="/film/The_Barber_l_homme_qui_n_etait_pas_la/497832/critiques">7.3</a>
                            <span data-sc-filter="rating,is_recommend,is_wish_list_or_shopping,is_current" title="" data-sc-product-id="497832" data-rel="sc-modal-listing-activity scouts-rating" data-sc-tooltip="true" class="erra-scouts d-posterRating-scout" data-sc-tooltip-text="Vos éclaireurs : 10 avis">6.9</span>
                        </div>
                        <div data-sc-zone-tag="btsc" data-sc-product-id="497832" data-sc-collection-id="525535" data-rel="sc-button" class="erra-currentuser">
                            <div class="erra-other-actions" data-sc-action-container="other"><span data-sc-action="wish-list" data-rel="other-action" class="eins-wish-list  green erra-other-actions-item only-child" style="display: inline-block; width: 16px; opacity: 1;"></span></div>
                            <div data-sc-action-container="main" class="erra-action"><span data-sc-action="rate" data-rel="sc-action" class="erra-action-item">6</span><span data-sc-action="wish-list" data-rel="sc-action" class="eins-wish-list white erra-action-item erra-action-item"></span></div>
                        </div>
                    </div>
                </div>
            </div>
        </li>
        ''')

    def test_get_authors(self):

        #With empty bs instance get_authors must return an empty list
        author_list = scscrapper.get_authors(self.empty_bs_instance)
        self.assertIs(type(author_list), list)
        #empty lists are evaluate to false
        self.assertFalse(author_list)


        #If authors wrapper is found but no authors inside get_authors must return an empty list
        author_list = scscrapper.get_authors(BeautifulSoup('<span class="ellp-baseline-a"></span>'))
        self.assertIs(type(author_list), list)
        self.assertFalse(author_list)


if __name__ == '__main__':
    unittest.main()