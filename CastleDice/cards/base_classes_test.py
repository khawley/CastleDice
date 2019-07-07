import unittest

from .base_classes import BaseCard
from .base_classes import ResourceCost
from .base_classes import CastleDeckMixin
from .base_classes import MarketDeckMixin
from .base_classes import VillagerDeckMixin
from .base_classes import NormalDiscardMixin
from .base_classes import NoBuildMixin
from .base_classes import NoDescriptionMixin
from .base_classes import NoOngoingMixin
from .base_classes import NoScoreMixin
from .base_classes import GatherPhaseMixin
from .base_classes import BuildPhaseMixin
from .base_classes import ChoosePhaseMixin
from ..common import Resources
from ..common import VillagerCards


class ResourceCostTest(unittest.TestCase):
    def test_success(self):
        wood_cost = ResourceCost(Resources.WOOD, 3)

        self.assertEqual(wood_cost.resource, Resources.WOOD)
        self.assertEqual(wood_cost.amount, 3)


class BaseCardTest(unittest.TestCase):
    def test_abstract_requires_all_the_things(self):
        parents_tests = [
            (GatherPhaseMixin, CastleDeckMixin, NoOngoingMixin, NoBuildMixin, NoScoreMixin),
            (BuildPhaseMixin, MarketDeckMixin, NoOngoingMixin, NoBuildMixin, NoScoreMixin),
            (ChoosePhaseMixin, VillagerDeckMixin, NoOngoingMixin, NoBuildMixin, NoScoreMixin),
            (NoScoreMixin, NormalDiscardMixin, NoDescriptionMixin),
        ]

        for parents in parents_tests:
            class ImplementedCard(*parents, BaseCard):
                pass

            with self.assertRaises(TypeError):
                ImplementedCard()

    def test_implemented_all_the_things(self):
        class ImplementedCard(
            GatherPhaseMixin,
            MarketDeckMixin,
            NormalDiscardMixin,
            NoBuildMixin,
            NoDescriptionMixin,
            NoOngoingMixin,
            NoScoreMixin,
            BaseCard
        ):
            _constant = VillagerCards.WISE_GRANDFATHER

            def description(self):
                return "Some description"

            def is_playable(self):
                return True

            def play(self):
                return

        self.assertTrue(ImplementedCard())

        card = ImplementedCard()
        self.assertEqual(card.card_id, VillagerCards.WISE_GRANDFATHER)
        self.assertEqual(card.name, "Wise Grandfather")
