import numpy as np


def input_number(prompt: str):
    try:
        number = int(input(prompt))
        return number
    except ValueError:
        pass


def throw_dice(number_of_dice: int = 1, sides: int = 6):
    """
    :param number_of_dice: How many dice to dice_list. None is captured.
    :param sides: Defaults to a 6-sided die. None is captured.
    :return: Returns a list of thrown dice.
    """
    number_of_dice: int = 1 if number_of_dice is None else number_of_dice  # Catch nulls.
    sides: int = 6 if sides is None else sides  # Catch nulls.

    dice_list = [np.random.randint(1, sides + 1) for die in range(1, number_of_dice + 1)]
    return dice_list


character_setup_list = ["Motywacje postaci",
                        "Zaczyn łazikowania",
                        "Rozwój postaci",
                        "Przyjazne frakcje",
                        "Aktywa i sprzymierzeńcy",
                        "Przedmioty magiczne i znaczące",
                        "Organizacje przeciwne",
                        "Rywale i wrogowie",
                        "Miejsca pobudzające wyobraźnię",
                        "Tematyczne potwory",
                        "Haczyki narracyjne i ziarna opowieści"]

archetype_list = ["Akolita", "Akrobata", "Zaklinacz zwierząt", "Archiwista", "Rzemieślnik", "Artysta", "Barman",
                  "Adwokat", "Łowca nagród", "Szarlatan", "Kucharz", "Przestępca", "Kultysta", "Detektyw", "Wysłannik",
                  "Artysta estradowy", "Wygnaniec", "Odkrywca", "Rolnik", "Bohater ludowy", "Wróżbita", "Hazardzista",
                  "Gladiator", "Grabarz", "Strażnik", "Zielarz", "Pustelnik", "Myśliwy", "Rycerz", "Robotnik",
                  "Uczeń sztuk walki", "Kupiec", "Medyk", "Górnik", "Szlachcic", "Koczownik", "Obcy", "Pirat",
                  "Pielgrzym", "Więzień", "Mędrzec / uczony", "Marynarz", "Uczony", "Zwiadowca", "Żołnierz", "Szpieg",
                  "Nauczyciel", "Majsterkowicz", "Ulicznik", "Wojownik", "Dziwak"]

acolyte_drives = {1: "Spread the beneficence of their deity",
                  2: "Rise to a leadership position in their order",
                  3: "Found a temple to spread their god's reach",
                  4: "Take a pilgrimage to a lost sacred site",
                  5: "Convert others to the fold through acts",
                  6: "Work miracles in the name of their deity",
                  7: "Leave a legacy like the saints in their texts",
                  8: "Preserve the faith by combating corruption",
                  9: "Embody the teachings, become an avatar",
                  10: "Unravel the mysteries of their faith",
                  11: "Forge connections with other religions",
                  12: "Shape the direction of their faith",
                  13: "Protect creation from corruption",
                  14: "Confront the sworn enemies of their god",
                  15: "Be fiercely loyal to their faith's principles",
                  16: "Redeem themselves for their past",
                  17: "Fulfill the prophecy, O chosen e",
                  18: "Retrieve the Sacred Relics or Artifacts",
                  19: "Strengthen their connection to the divine",
                  20: "Prove their worth in the eyes of their god",}
acolyte_catalysts = {1: "Divine vision in dreams or meditation",
                     2: "A sacred messenger came calling",
                     3: "Ancient text holding suppressed knowledge",
                     4: "Signs and portents hint at prophecy",
                     5: "Divine power implies worldly responsibility",
                     6: "Heretical sect just might be onto something",
                     7: "Fanaticism threatens to define their faith",
                     8: "Assigned a mission by the elders",
                     9: "Ritualistically initiated into a secret order",
                     10: "Internal corruption threatens their faith",
                     11: "Entrusted with a significant relic",
                     12: "A distraught pilgrim begs for their help",}
acolyte_growth = {1: "Submissive servant, to empowered leader",
                  2: "From sinner, to saint",
                  3: "Blind follower, to free thinker",
                  4: "Simplistic understanding, to sophisticated",
                  5: "Riddled with doubt, to firm in belief",
                  6: "Extremely sheltered, to experienced and worldly",
                  7: "Strictly dogmatic, to progressive reformer",
                  8: "Untested novice, to tempered and wise",}
acolyte_friends = {1: "The Gardens of Serenity: Vineyard & Abbey keeping a vow of silence and a powerful secret",
                   2: "Shields of Faith: Holy warriors who devote themselves to martial arts and the deity's ways",
                   3: "The Wayfarer's Star: A merchant's guild promoting and profiting from a pilgrimage path",
                   4: "Shadows of the Sacred Flame: Spies who infiltrate and monitor secular organizations",}
acolyte_assets = {1: "Elahandra of the Radiant Veil: Wise and benevolent leader weary of internal politics",
                  2: "Brother Galen: An ancient acolyte who never advanced, brimming with rumors",
                  3: "Atticus the Elder: Bespectacled Scribe with encyclopedic knowledge of the faith's history",
                  4: "Marcum Veldar: A noble who supports the order to compensate for personal debauchery",
                  5: "Orek the Wanderer: Splintered from the authorities, walks the world healing people",
                  6: "Sister Isolde: Eccentric, slightly scattered, and kindly devotee with erratic gift of prophecy",}
acolyte_items = {1: "Well-worn Journal or Annotated Scripture: written by mentor or an historical figure",
                 2: "Vestments of Authority: Symbolic outfit that will greatly impress some and anger others",
                 3: "Chalice of the Faithful: Removes poison from any liquid put within it, once per day",
                 4: "Clarifying Lens: Piece of stained glass from ancient temple that can pierce illusions",
                 5: "Beads of Answered Prayers: Increases odds of successful divine intervention",
                 6: "Pealing Retribution: Inscribed bell or singing bowl, deafens all others in range",
                 7: "Holier Symbol: Improves potency of any magic under the deity's divine domain",
                 8: "Staff of the Hierophant: Summons an allied celestial creature for aid, once per week",
                 9: "Crown of Blessings: When activated hovers like a halo and gives off light as candle or torch",
                 10: "Angelic Amulet: Made of mysterious material, reduces damage of specific types",}
acolyte_antagonists = {1: "House of Blessed Respite: Posing as a hospice, but collecting dead for nefarious reasons",
                       2: "The Salted Earth: Clandestinely disrupting rituals and undermining faith to “clear the way”",
                       3: "Cult of the Stranger: Worship a forgotten god unaware it is a well-known demon",
                       4: "Serpentine Sect: Corrupt clergy who use their influence for personal gain and pleasure",
                       5: "The Reliquary Raiders: Dungeoneers who find and loot ancient holy sites for profit",
                       6: "The Prophet's Children: A splinter sect thought to be harmless which proves to be anything but",}
acolyte_rivals = {1: "House of Blessed Respite: Posing as a hospice, but in truth collecting dead for nefarious evils",
                  2: "Salted Earth: Clandestinely disrupting rituals and undermining faith to “clear the way”",
                  3: "Cult of the Stranger: Worship a forgotten god unaware it is a well-known demon",
                  4: "Serpentine Sect: Corrupt clergy who use their influence for personal gain and pleasure",
                  5: "The Reliquary Raiders: Dungeoneers who find and loot ancient holy sites for profit",
                  6: "Prophet's Children: A splinter sect thought to be harmless which proves to be anything but",}
acolyte_locs = {1: "Hidden Shrine: Far from civilization, overgrown and long reclaimed by nature",
                2: "Inner Sanctum: Hidden area secretly accessed from within a public temple",
                3: "The Catacombs: Entombed clergy and saints, likely relics and guardians as well",
                4: "Floating Temple: Ship traveling by sea or air to major cities and remote lands",
                5: "Celestial Observatory: Group of acolytes studying the heavens for signs and portents",
                6: "Pillars of Divinity: Natural structures or remnants of a giant edifice, considered holy by many",}
acolyte_monsters = {1: "Fallen Angel: An avatar of the deity corrupted by evil, to be purified or battled",
                    2: "Dark Templars: Antipaladins who embrace pure power as their highest and only ideal",
                    3: "Ghostly Apostate: The spirit of a dead follower who feels wronged by the deity",
                    4: "Blasphemous Construct: Soulless machine created to destroy divine servants",
                    5: "The Inquisitors: Judges who made a pact with a devil, trading undeath for guilty souls",
                    6: "Dark Abomination: Ancient eldritch horror older than the gods who resents their creations",}
acolyte_plot_hooks = {1: "Renovations reveal the temple sits on top of the entrance to another site, perhaps sealing it",
                      2: "A religious artifact has been uncovered that can be very dangerous in the wrong hands",
                      3: "The prophecy foretells the coming end of the world, and how to postpone it",
                      4: "There's a plan to disrupt an innocent seeming holiday tradition, but it's actually the key to peace",
                      5: "A sacred text has been stolen, containing a ritual for summoning beings from other planes",
                      6: "A group of pilgrims have been taken hostage and need to be rescued before it's too late",
                      7: "Something's very wrong with the leader of the order, but few are brave enough to say so",
                      8: "The Chosen One has been found, it's not you, it's a child and you must protect it",
                      9: "A fellow acolyte sends a cryptic note about a mysterious mission before they disappear",
                      10: "A long forgotten sect returns to warn of a great danger approaching, but no one is listening",
                      11: "A mentor stands accused of heresy and you must prove their innocence, or guilt",
                      12: "The origins of the faith, or their deity itself, is not what everyone believes it to be",
                      13: "Their deity loses their divinity and as a mortal asks for aid to get it back",
                      14: "Celestial Servants seek to stage a coup, they may have a point, but any war will be devastating",
                      15: "The order was entrusted to keep an ancient evil slumbering, but doesn't remember how exactly",
                      16: "Gods are going missing, their followers are losing their powers, & the cause is yet unknown",
                      17: "A former friend has been converted to an evil deity's domain and become powerful in the process",
                      18: "Hidden texts reveal their god replaced an earlier deity, there are conflicting theories as to why",
                      19: "The largest temple or holy city is suddenly, inexplicably, totally empty",
                      20: "Everyone looks to the acolyte as a representative of their faith, expecting them to act accordingly",}

acrobat_drives = {1: "Earn respect and recognition for skills",
                  2: "Protect the honor and code of the carnival",
                  3: "Bring joy, delight, & relief from the mundane",
                  4: "Ultimate Freedom, of movement and all else",
                  5: "Get rich before they can no longer perform",
                  6: "Become famous and a source of awe",
                  7: "Defy death to feel truly alive",
                  8: "Push the limits of what is thought possible",
                  9: "The show must go on, no matter what",
                  10: "Family is everything & the troupe is family",
                  11: "Prove they are far beyond the average",
                  12: "Courage only comes when facing fear",
                  13: "Talent is nothing without dedication",
                  14: "The world is to big to ever stop exploring",
                  15: "True failure comes from never trying",
                  16: "Limits exist to be pushed past & overcome",
                  17: "It's not the strongest survive, it's the flexible",
                  18: "You're only as good as your last act",
                  19: "Life is short so you better leave a legacy",
                  20: "Only the greatest can inspire greatness",}
acrobat_catalysts = {1: "The couldn't run away & join the circus, so...",
                     2: "A loved one fell and they must atone for it",
                     3: "It's amazing what you can learn traveling",
                     4: "It's been the family business for generations",
                     5: "A childhood fall revealed their innate abilities",
                     6: "The thrill is gone and they need a challenge",
                     7: "They can, they should, so they must",
                     8: "The troupe is under threat only they can face",
                     9: "A friendly rival became an adventurer first",
                     10: "Performing at court they saw they can help",
                     11: "A wealthy patron funds their new exploits",
                     12: "Seeking revenge for childhood tragedy",}
acrobat_growth = {1: "Battling stage fright, to comfortable confidence",
                  2: "From falling flat, to soaring high",
                  3: "A fear of heights, to fearlessness",
                  4: "From solo act, to group performer",
                  5: "Falling only to rise again",
                  6: "Rigid and unyielding, to fluid and flexible",
                  7: "Recklessness, to courageous awareness",
                  8: "From protege, to expert, to mentor",}
acrobat_friends = {1: "The Swooping Swallows: The found family troupe they toured with for years",
                   2: "The Ring of Masters: A loose network of circus artists sharing information and aid",
                   3: "Perfection in Motion: A group of ascetics who perform acrobatics as a spiritual practice",
                   4: "The Sweep Chimneys: Clandestine group for hire, use their dexterous skills to spy or steal",}
acrobat_assets = {1: "“Silky” Remaud: An alluring silk dancer who learns much from her cadre of rich suitors",
                  2: "Ardus Cain: A barker who runs a freak show to provide for and protect his wards",
                  3: "“Tall” Jorga: A tremendously large strongman who's surprisingly wise and light on his feet",
                  4: "Lady Emerlade: A well-connected noble who's a great patron of the performing arts",
                  5: "Whisper: A mummer who never says a word but is always listening",
                  6: "Pietro “Second Story:” An old troupe member who now finds crime much more lucrative",}
acrobat_items = {1: "A faded poster from an old performance, which was someone's last night in the act",
                 2: "A small music box that will play a calliope if they can find someone to repair it",
                 3: "Chalk of the Aerialist: Provides a temporary boost to gripping, climbing, and swinging",
                 4: "Feather Fall Charm: Can slow a fall to prevent damage once per day",
                 5: "Collapsible Balancing Pole: Only 8” long but expands to 10' and aids in balancing",
                 6: "Magic Slack Line: 50' of rope that magically extends and ties itself to anchor point if it can",
                 7: "Barker's Wand: Can magically produce illusory sparkles or amplify the voice at will",
                 8: "Cloak of the Flying Squirrel: Can glide 30' horizontally for every 10' fallen",
                 9: "Tunic of the Tumbler: Provides a small increase in armor without hampering mobility",
                 10: "Air Dancer's Arrow: Leaves a golden thread behind it that can be balanced on to the target",}
acrobat_antagonists = {1: "Jester's Court: Guild that tightly controls who performs in places and high society circles",
                       2: "Concerned Commoners: Distrust and drive off all traveling performers and “freaks”",
                       3: "Fleabag Circus: Traveling performers whose show is a distraction for thieves & pickpockets",
                       4: "Local City Watch: Suspects them of every crime for no reason, it's just profiling",
                       5: "Obsessive Fan Club: Appear at inconvenient times with no regard for danger or boundaries",
                       6: "The Puppet Masters: A carnival where all the acts are enchanted and forced to perform",}
acrobat_rivals = {1: "Antigravity Bael: Claims to be the greatest of all acrobats, suspected of sabotaging others",
                  2: "Sdu Pendez: Collects and trains big cats for performances, questionable ethics and hygiene",
                  3: "Lord Vence: Betrothed ran off with a circus performer and now he hates anyone associated",
                  4: "The Iron Monger: Strongman bully who moonlights as thug enforcer when they can",
                  5: "Lady Evangeline: Noble who's jealous of mobility and freedom, employs crooked guards",
                  6: "Ashen Fetik: Wizard with a penchant for traps that rely on illusions and gravity flipping",}
acrobat_locs = {1: "The Grand Cirque: A small stripped tent that is extradimensionally huge inside",
                2: "The Gauntlet: An ancient obstacle course designed to let only the worthiest pass through",
                3: "The House of Rising Fountains: a wizard's manse where gravity is unpredictable",
                4: "The Sinking Forest: the ground is a sucking mire, the only way through is vines & branches",
                5: "Moonlit Menagerie: Mysterious carnival filled with delights & potentially dangers",
                6: "Old Suspension Bridge: Long neglected and could go any minute, can't beat the classics",}
acrobat_monsters = {1: "Giant Flying Squirrels: Cute but very sharp claws, fey use them for mounts",
                    2: "Stone Gargoyles: Attack anything above the roof line, grappling and falling like stones",
                    3: "Gravitas: Earth elemental who can create gravity waves and induce vertigo",
                    4: "Fear Monger: Shadowy specter that feeds on fear and can terrify targets to death",
                    5: "Arachnamod: Climbing construct of eight arms attached in a spider-like configuration",
                    6: "Net Gremlin: Small with prehensile tails, cut safety nets, throw nets and poison darts",}
acrobat_plot_hooks = {1: "A floating city of the lost age has drifted near, exploring it will be a challenge for the most nimble",
                      2: "A monster has built it's nest high on the wall inside a huge chimney, making it difficult to reach",
                      3: "A fey court is snatching performers & artists to force them to be entertainment at endless parties",
                      4: "The heist will likely require a dexterous infiltration by a character, who can then let the rest in",
                      5: "Traveling between towns, the acrobats old troupe has disappeared on a stretch of road in the wilds",
                      6: "The easiest way to get into the same room as the emperor is to join the line of courtly entertainers",
                      7: "Someone has stolen the acrobat's act and identity, maybe using their reputation or framing them",
                      8: "An old mentor has died performing a notoriously risky feat, but there are rumors of foul play",
                      9: "An ethereal figure begins appearing whenever the character displays acrobatic prowess",
                      10: "Vines are the only things connecting the floating islands of the blighted Sky Gardens",
                      11: "The Night Circus only appears on the full moon, much can be gained and lost at the games of skill",
                      12: "The pendulum trap took out the bridge and now using it as a trapeze may be the only way across",
                      13: "This town celebrates the daredevils who braved the nearby dungeon, at least, the ones who lived",
                      14: "While the shelves remain attached to the walls, the floors of the towering library are long gone",
                      15: "A circus owner is paying well for young magical beasts they can add to their menagerie",
                      16: "The family troupe has been cursed, and are spreading the affliction as they travel town to town",
                      17: "The Giant's Orrery is filled with gems and precious metals, among its whirring clockwork gears",
                      18: "Returning the dragon's egg and ending the rampage will mean ascending to treacherous heights",
                      19: "The mage opened a portal to the elemental plane of fire and now the floor is lava",
                      20: "It's said the ghost ship will keep reappearing until someone climbs the rigging to the crows nest",}

animal_whisperer_drives = {1: "Fulfill the debt to animals after one saved life",
2: "Learn the wisdom of Nature",
3: "Speak the language of every beast",
4: "Earn enough to create a sanctuary",
5: "Maintain the delicate balance of all life",
6: "Root out the unnatural wherever it is found",
7: "Protect endangered beasts large and small",
8: "Carve out a space for a wildlife refuge",
9: "Serve as a bridge between species",
10: "Discover and document new forms of life",
11: "Track down the storied beasts of legend",
12: "Searching for a magical lost pet",
13: "Gain fame and use it to educate the masses",
14: "Catch and release every beast for the thrill",
15: "Prove they are the supreme apex predator",
16: "Gain notice and favor of animalistic deities",
17: "Conserve natural order by hunting invasives",
18: "Emulate the power and nobility of beasts",
19: "Get in touch with the purity of the primal",
20: "Be a voice for the beasts that can't speak",}
animal_whisperer_catalysts = {1: "Animal companion is their first & only friend",
2: "An atavistic beast spoke to them",
3: "Witnessed technology's devastation to wilds",
4: "Visions & fever dreams after venomous bite",
5: "Deeper meaning revealed within birdsong",
6: "Abandoned in the wilds & raised by animals",
7: "Culture of totemic reverence for beasts",
8: "Unknowingly stumbled into a druidic ritual",
9: "A tome of animal facts is their entertainment",
10: "Betrayed by all except a loyal pet",
11: "Relates to the feared, misunderstood beasts",
12: "Messages revealed in animal behaviors",}
animal_whisperer_growth = {1: "Practically feral, to acclimated in society as well",
2: "Lone wolf type, to integral pack member",
3: "Balancing their animal and humanoid sides",
4: "From trophy collector, to conservationist",
5: "From isolated traveler, to community educator",
6: "Distrusted outsider, to celebrated hero",
7: "Toxic “Alpha” type, to integrated & wise leader",
8: "Shy around all but animals, to quiet confidence",}
animal_whisperer_friends = {1: "The Keepers: Rangers and hunters who live off the land and protect the balance of nature",
2: "Owlbear Collective: Isolated forest commune who eschews arcana, tech, and clothing",
3: "Skinwalkers: Enclave of druids most comfortable wildshaped into animal forms",
4: "Sasquatch Society: Cryptid seekers, though most are just there to hike and socialize",}
animal_whisperer_assets = {1: "A cadre of cute woodland creatures who are helpful but constantly sing annoying songs",
2: "'Falcon' Haux: Trains birds of prey & secretly sees through their eyes, very reticent to people",
3: "Bramble Doon: Chatty herbalist who heals animals as well as people, gossips with both",
4: "Yara Sulincar: A scholar studying beasts, oozes, and monstrosities, filled with trivia",
5: "Grok: Hyper-intelligent crow adept at mimicry, could be more to him than it seems",
6: "Ret Hester: Vagabond secretly struggling with lycanthropy, self-medicates with booze",}
animal_whisperer_items = {1: "A feather on a leather band, a gift from the only person they loved as much as animals",
2: "A hand illustrated bestiary that contains information on a wide range of creatures",
3: "Collar of Communication: Grants speech to the animal wearing it, intelligence is unaffected",
4: "Enticing Treats of Enlargement: Enough to cause",
3: "beasts to increase in size for 6 hours",
5: "Soothing Flute: Sends beasts into a swaying catatonic state when played",
6: "Eye of Fenrir: Can intimidate, tame, and see through the eyes of a beast, 1 use per day each",
7: "Hunter's Horn: Causes all beasts in range to panic except trained animal companion",
8: "Pawprint Pendant: Magically highlights tracks and trails from the last 3 days",
9: "Sacred Totem: Channels powers of depicted animal, boosting an ability for 1 hour",
10: "Enchanted Statuette: When attuned can summon a beast equal to half their current level",}
animal_whisperer_antagonists = {1: "The Gilded Cage: A zoo accessible only by the very wealthy, known to mistreat its animals",
2: "The Horned Cartel: Black market selling parts of poached animals for questionable ends",
3: "Kleer Consortium: Group practicing clear cutting, strip mining and other extreme methods",
4: "Cult of the Fang: Seeks out the most poisonous beasts they can find for their rituals",
5: "Binky Brigade: Misguided rabbit lovers who kill off all predators & thus population explodes",
6: "Koalaseum: Hosts cruel animal fights taking percentage of all wagers",}
animal_whisperer_rivals = {1: "Baron “The Butcher” Swift: Big game trophy hunter, said to have bagged a unicorn recently",
2: "Klade Vendal Colme: Serial killer who targets beasts between killing humanoids",
3: "Perquin the Magnificent: Mage creating monstrosities through animal experimentation",
4: "Ro'Dencia Vane: Infiltrates high society to case heists performed by her trained rats",
5: "Hyde Thorne: Polymorphs into beasts to do heinous crimes, creating violent backlash",
6: "Cantor Sparrowtail: A bard who uses caged birds in act, “disappearing” one as the encore",}
animal_whisperer_locs = {1: "Zootopia: Long fallen city which had a large zoo, decedents of those animals abound here",
2: "Jungle Primeval: Untouched by civilization, creatures thought extinct or only myth hunt here",
3: "Cradle of the Wyld: Lush valley sacred to druids somehow corrupted, spawning monsters",
4: "Wetlands of Woe: Necromatic forces deep in this marsh generate wandering undead beasts",
5: "Coral Tower: Filled with sea water, teeming with hostile aquatic life and treasure",
6: "Clockwork Wood: Mad Gnomes have created mechanical beasts who run amok here",}
animal_whisperer_monsters = {1: "Ghost pack: Ethereal wolves whose haunting howls induce overwhelming fear",
2: "Chimera and other magically made monstrosities of patchwork animal parts",
3: "Verdant Vengeance: Fey spirit who commands wild beasts, & animal companions",
4: "Diamond dogs, fire birds, wind serpents, water bears, & other elemental beast hybrids",
5: "Mirrorshell: Huge tortoises with powerful jaws and shells that can reflect magical attacks",
6: "Depressed beasts of burden & abused mounts of hostile humanoids, potential to tame",}
animal_whisperer_plot_hooks = {1: "Mauled corpses of exotic beasts create a wave of fear, evidence of an illegal fighting ring in town",
2: "A wealthy noble will pay well to thwart his rival's trophy hunt and protect the beast in question",
3: "The song of a rare bird is the only method to open the sealed doors of the dungeon",
4: "Rash of unusually aggressive animals and a series of attacks points to an evil influence in the wild",
5: "Someone is using animals as a vector to spread a mysterious disease",
6: "A child seems able to command beasts, the locals (wrongfully) fear it's a sign of demonic influence",
7: "Animal messengers seek out the party to enlist their aid directly in clearing an evil humanoid tribe",
8: "A tremendous beast, remnant of an age long past, is the only creature who may still remember",
9: "Family pets and farm animals alike are running away to a cave entrance that opened nearby",
10: "People are reporting tiger attacks a thousand miles away from where any tiger should be",
11: "A tribe thought to be primitive has tamed dinosaurs and are using them to expand their territory",
12: "He said he was collecting bones to render glue, but then the patchwork animal skeletons attacked",
13: "A pod of killer wales have started attacking ships and effectively blockade the harbor",
14: "The sovereign's pet bear has begun to act erratically, magical foul play is suspected",
15: "Shrunken to the size of insects, which are now a huge threat until a cure is found",
16: "An annoying squirrel that won't leave the party alone is actually the polymorphed monarch",
17: "The sewer rats chewing their way into homes and stealing gold are in fact a gang of wererats",
18: "A tremendous boar driving woodsman away is protecting a sacred site from discovery",
19: "A celestial beast of swirling stars has arrived to aid threatened animals and restore balance",
20: "To successfully deliver the McGuffin, the party will have to travel by a series of exotic mounts",}

archivist_drives = {1: "Seek out and uncover hidden truths",
2: "Preserve the knowledge of generations past",
3: "Uphold the duties of the librarian lineage",
4: "Most evil in the world is rooted in ignorance",
5: "Discover things worth adding to the archive",
6: "Codify the magical forces in the world",
7: "Collect exotic samples and specimens",
8: "Do deeds worthy of the written word",
9: "Add entries to the bestiary by experience",
10: "Prove knowing is at least half the battle",
11: "Learn about the real world directly for once",
12: "Uncover wisdom hinted at within tomes of old",
13: "Spread peace & safety so scholars flourish",
14: "Demonstrate the learned should lead",
15: "Experience new cultures, current and lost",
16: "Unlock a mystery to prevent a disaster",
17: "Seek out forbidden lore to gain power",
18: "Establish the greatest library in all history",
19: "Important things have been forgotten",
20: "Truth will set you free if you're brave enough",}
archivist_catalysts = {1: "Books are burning but truth must prevail",
2: "Rumors of an unknown civilization's legacy",
3: "A trove of new scrolls hints at more to find",
4: "Their people were exploited from lack of info",
5: "There is a mysterious map in the archive",
6: "A secret door reveals a hidden codex",
7: "They are the only one with the know-how",
8: "An apprentice is raising valid questions",
9: "A critical mass of knowledge bends reality",
10: "Potentially dangerous texts are missing",
11: "An ancient scribe's marginalia is troubling",
12: "Bibliomancer's prophecy names them",}
archivist_growth = {1: "Strictly theoretical, to applied knowledge",
2: "Ivory tower, to one of the common people",
3: "Outer knowledge, to knowledge of self",
4: "Obsessive collector, to synthesizing curator",
5: "Consuming knowledge, to spreading it",
6: "Shut in, overcoming fear to explore the world",
7: "Balancing intellect with emotions (IQ vs EQ)",
8: "Studying book scraps, to questioning the gods",}
archivist_friends = {1: "Eternal Word Abbey: Monastic order of scribes with ages of knowledge preserved",
2: "Silverleaf Circle: Preserve and perpetuate folk knowledge through oral tradition",
3: "Illuminati: Guild of artists who illustrate manuscripts, know location of many texts",
4: "Codex Custodians: Restore aged and damage books, sometimes miraculously",}
archivist_assets = {1: "Hermann Aelier: Performs divination by automatic writing & scries with pools of ink",
2: "“Misty” Shores: Bard who swaps stories from her travels for archive access & inspiration",
3: "The Ghostly librarian: Can find anything in the stacks if they like you, strictly enforces quiet",
4: "Minafred Stole: Eccentric noble who donates to the archive, mostly interested in astrology",
5: "“Inkyfingers” Zok: Sells the best archival ink, proceeds fund weird alchemical experiments",
6: "Kalen Currin: Merchant who trades in rare books & moonlights as a fence for thieves",}
archivist_items = {1: "The cracked spectacles of the mentor who taught them to read and write",
2: "An incredibly valuable first edition of a popular book, written in authors own hand",
3: "The Boundless Book: Blank book, pages that are torn from it regenerate",
4: "Lunar Quill: Messages written with this are only visible in the light of a full moon",
5: "Lens of Comprehension: Translates written language but can't decode or break encryption",
6: "Tome of Tongues: A week of study grants fluency in a new language",
7: "Helping Friendly Book: Incredibly chipper sentient tome that provides advice at random",
8: "Archival Tags: Identifies any object it is adhered to, each is one time use as words stay",
9: "Sanctum Librarium: A book that is actually a door to a library in a pocket dimension",
10: "Entangled Texts: Pair of identical books, what's written in one appears in the other",}
archivist_antagonists = {1: "Censor Caesura: Radical wizards who fear arcane knowledge falling into the wrong hands",
2: "Avendale Empire: Aggressively mobilizes citizens with a fabricated history to avenge",
3: "Vulpine Scribes: Disseminate propaganda & disinformation to sow chaos and weaken state",
4: "The Darkchive: Amassing a collection of evil treatise, forbidden knowledge, & dark magics",
5: "Divine Oblivion: Believe ignorance is bliss, attempting to bring world “back to basics”",
6: "The Common Core: Think education corrupts children & seek to eradicate learned “elites”",}
archivist_rivals = {1: "Unseen University: Wizard College whose library is expertly run by an orangutan",
2: "Whispering Wood: The oldest trees are carved in runes, detailing a lost history",
3: "The August Anathaeum: Temple to a goddess of wisdom hiding many artifacts",
4: "Sunken Scriptorium: Top of tower sticks out of desert sand, filled with knowledge & owls",
5: "Curio Crossing: Flea market of many vendors selling antiques, scrolls, knickknacks, & junk",
6: "Literati Tomb: A dungeon filled with word searches, scrambles, and other puzzles",}
archivist_locs = {1: "Sylex Vern: Ruthless “treasure hunter” who takes texts from tombs, dungeons, and libraries",
2: "Marlova Finn: Expert forger whose passed off several fake books and is available for hire",
3: "Lord Commander: Sovereign who burns books to enforce his doctrine of supremacy",
4: "Devon Rey: Hosts a private museum filled with fakes, forgeries, and ill-gotten goods",
5: "Lupin Bloodwell: Pen name of mysterious author whose works are inducing madness",
6: "Henri Walton: Adventurer who leaves his calling card where he's already looted treasure",}
archivist_monsters = {1: "Smoldering Mephit: Elemental who derives joy from burning things, especially books",
2: "Bookwyrm: Tiny drakes who breed inside books and consume paper, bane of all archives",
3: "Papyrophage: Eat meaning, devouring words & excreting empty symbols onto pages",
4: "Book Mimic: Grow to impersonate bookcase, and stories say even full libraries in rare cases",
5: "Ink Kraken: Many-tentacled sea monster who can release a cloud of magical darkness",
6: "Xalmora: A wizard bound this demon to a book from which it still spreads its evil",}
archivist_plot_hooks = {1: "Fire has gutted the archive, arson is suspected, perhaps to cover the tracks of a theft",
2: "Generally information should be free but some knowledge is very dangerous in the wrong hands",
3: "A writer's devoted following starts to imbue them with magical powers, which goes to their head",
4: "A scribe has discovered all pages regarding a specific location have been ripped out of the books",
5: "Scholars in a certain subject area are disappearing, can they reach the last one before it's too late",
6: "An ancient wizard tower has been discovered starting a race for their legendary grimoires",
7: "A mysterious curse is spreading and the only way to find a cure would be through research",
8: "It's trivia night at the tavern, though must are unaware the stakes are incredibly high tonight",
9: "A cache of tablets has been uncovered describing advanced technology, including weaponry",
10: "As a deceased noble's estate is packed up, their library reveals they were studying dark magics",
11: "Obscure manuscript containing an enigmatic prophesy comes to light, deciphering it is a challenge",
12: "A city is under siege, threatening the citizens inside as well as a pair of significant museums",
13: "Someone has stolen a minor, seemingly ordinary artifact, while leaving much more valuable treasure alone",
14: "The archive is secretly run by a clandestine society & they approach with a quest of initiation",
15: "A strange document resists translation, someone must contact the remote tribe of its origin",
16: "An evil god feels threatened by mortals accumulating too much knowledge, and sends its minions",
17: "A sentient book leads to ancient treasure-filled ruins, but it has an agenda of its own",
18: "An atlas of fictional locations is discovered to show an ancient sunken continent",
19: "The diocese's files contain blueprints to many important building in the city, which could be useful",
20: "An explorer was mapping a region one hex at a time, but all that was recovered was his journal",}

artisan_drives = {1: "Discover new styles and techniques",
2: "Explore the works of other peoples & eras",
3: "Hone their skills & pass on their craft",
4: "Change the way the world views their work",
5: "Find new and exotic materials to work with",
6: "Pay off the debts of a failed enterprise",
7: "Uncover lost secrets of their craft",
8: "Find new calling after their trade's collapsed",
9: "Fund a new workshop or trade school",
10: "Prove worthy of a rare apprenticeship",
11: "Gain recognition or fame that's eluded them",
12: "Gather artifacts & establish museum of craft",
13: "Collect magical tools & techniques",
14: "Live authentically to craft authentically",
15: "Achieve greatness over fears of mediocrity",
16: "Transcend tradition & innovate the form",
17: "Skillfully improve world however they can",
18: "Adventuring is honest work, & pays better",
19: "Seek out beauty & destroy ugliness/evil",
20: "Make an impact that transforms society",}
artisan_catalysts = {1: "An ancient piece reveals new levels of craft",
2: "Examples of their work are being destroyed",
3: "A manual of the craft holds secret knowledge",
4: "A commission requires rare materials",
5: "A mundane tool proves magic, & sentient",
6: "Asked to lend expertise at new-found ruins",
7: "A rival has taken to the adventuring life",
8: "Witnessed magic that could end their trade",
9: "A master craftsmen assigns an unusual task",
10: "A god of craft sends a messenger or vision",
11: "The guild hall has a prophecy it passes on",
12: "Works that convey much more than language",}
artisan_growth = {1: "From unknown laborer, to renowned master",
2: "Singular focus on a skill, to well-rounded",
3: "Valuing ideal forms, to valuing relationships",
4: "Mired in past tradition, to a creative innovator",
5: "From working to live, to living to work",
6: "Detailed perfectionist, to big picture thinking",
7: "Crafting commodities, to creating art",
8: "Cloistered & singularly obsessive, to worldly",}
artisan_friends = {1: "The Steel Hammer: League of smiths who expanded over time to include nearly all trades",
2: "Architects of Eternity: Temple builders who treat their craft as an act of devotion & worship",
3: "The Hall: Guild formed to represent artisans in government settings and trade negotiations",
4: "Monumentalists: Civic minded nobles funding public works, with their names on it of course",}
artisan_assets = {1: "Eldora Wheatley: An aged master of the craft who also has expertise in other areas",
2: "Curator Sirus: Forced formality as the head of an institution's collection, has an eye for value",
3: "“Scrapper” Braum: Gruff owner of a salvage shop with hidden gems among the junk",
4: "Guildmaster Thorguil: Influential leader with connections throughout society, high to low",
5: "Jirou “Dreamer” Hahn: Easily distracted apprentice who is eager to be of use",
6: "Althera Pown: Bookish scholar studying ancient means of methods of various trades",}
artisan_items = {1: "A well-worn tool, passed down through the generations, that they hope to pass on one day",
2: "A conceptual sketch from a mentor or hero, something's missing & it wouldn't work as is",
3: "Neutral Militia Multitool: Functions as most tool kits, with slight penalty to effectiveness",
4: "Crafter's Calipers: Can measure and identify most items, even magic items, in minutes",
5: "Extra Hand: Floats within 30' of attuned, carries light objects like torches, as mage hand",
6: "Enchanted Tool Bag: Small extradimensional space, floats objects out when named",
7: "Master's Set: Artisanal tools that grant bonus to skill and produce finest examples of craft",
8: "Measure Twice: Circlet that grants wearer precise knowledge of any distance they can see",
9: "Collapsible ladder: Magically extends from 1' to 25' for easy climbing, though it is slightly heavy",
10: "Scepter of Shaping: Once daily turns a 10' cube of material as moldable as clay for 1 minute ",}
artisan_antagonists = {1: "Facet Cutters: Jewelers who are a front for racketeers offering “protection” to the locals",
2: "The Invisible Hand: Nefariously corners the market on many materials to inflate prices",
3: "The Gilded Chain: Exclusionary guild that ruthlessly guards the secrets of their craft",
4: "Harmony Handicraft: Cut corners, exploit workers, & use faulty gear to maximize profit",
5: "Guild Busters: Nobel elite who fear collective bargaining is a threat to their wealth and power",
6: "Nature League: Raw-food, nudist splinter group against “non-natural” works of all kinds",}
artisan_rivals = {1: "Varjik Stonehand: Steals & ruins reputations by claiming others have stolen their ideas",
2: "Hephaestus: Constant smoldering anger, builds ovens, kilns, & forges, a secret arsonist",
3: "Carmak Thesalon: Hires artisans to work on his sprawling manse, finds pretexts to not pay",
4: "Garvus “The Vandal”: Sullen teen who defaces great artisanal works for kicks by night",
5: "Minten Sorrel: Mediocre craftsman who sabotages competition through abyssal deals",
6: "“Crazy” Zeb: Peddler who sells cheap faulty goods, including tools that can lead to injury",}
artisan_locs = {1: "Artisan Alley: Narrow street filled with sound & smells of industry by day, but crime by night",
2: "Abandoned Atelier: Dust-covered workshop hiding valuable secrets for any who understand",
3: "Elemental Ferry: Magical transport of goods (& occasionally creatures) from other planes",
4: "Resplendent Ziggurat: Filled with examples of ancient artisanal excellence, also traps",
5: "Bottomless Quarry: Network of mines and quarries that broke through to the underworld",
6: "Giant's Workshop: Magical works at a tremendous scale, standing nearly finished",}
artisan_monsters = {1: "Elemental Animus: Spirit from elemental planes that can occupy & animate a substance",
2: "Evil Architect: Provides other enemies with equipment, offensive, defensive, or magical",
3: "______ Golems: Constructs crafted of a relevant material, magically animated, serving a master",
4: "Gremlins: Small chaotic creatures who take joy in sabotage & destruction of other's work",
5: "Giant Mason Wasp: Create elaborate hive where they stuff paralyzed victims with eggs",
6: "Scrap Shardlings: Technically oozes, build crustacean like shells out of reclaimed materials",}
artisan_plot_hooks = {1: "A sinkhole swallows a worksite, someone should go down there before something crawls out",
2: "The restoration of an ancient artifact has activated a magical curse",
3: "No one is likely to be commissioning new work until peace & safety are restored",
4: "A restless spirit is causing chaos in the workshop, & it's getting more destructive",
5: "A new site from an ancient civilization known for excellence in their craft has been uncovered",
6: "One of the guilds has started playing dirty, unleashing destructive monsters to drum up business",
7: "Someone is snatching up artisans, it's assumed they must be building something sinister",
8: "An outdated way of doing things, thought to be empty ritual, turns out to be preventing disaster",
9: "There are rumors of a pocket of legendary crafting material in a difficult & dangerous location",
10: "A schematic for a powerful artifact is discovered, sparking a race to hunt down the components",
11: "A piece that's been the pride of the town has disappeared, could it have got up and walked away?",
12: "Approached to repair an act of vandalism, turns out it was not the work of local teens as assumed",
13: "Someone tried to cheat & win a competition with a trained mimic, it ate them and is now at large",
14: "A monstrous incursion halts the flow of natural resources required for their craft to progress",
15: "A high-end good coveted by the rich & powerful is being used to scry on the seats of influence",
16: "An ancient master's work breaks, revealing a secret hiding in plain sight for centuries.",
17: "An eccentric local's work was thought bizarre but harmless, until the gateways started opening",
18: "The legend that giant's built the region's landmark wasn't taken seriously, until the giants returned",
19: "A magic that could replace all artisans has been developed & threatens to spin out of control",
20: "An apprentice has been moonlighting to make ends meet and has gotten into deep trouble",}

artist_drives = {1: "Desire to have constant unique experiences",
2: "Create their masterpiece",
3: "Art's highest calling is to confront oppression",
4: "Ensure preservation of art in all forms",
5: "Draw inspiration from new locations",
6: "Discover anything new under the sun",
7: "Beautify the world by destroying evil",
8: "Earn enough gold to fund their big project",
9: "Inspire change through art and acts",
10: "Become immortalized however they can",
11: "Bring peace through their art",
12: "Inspire works of art through their deeds",
13: "Collect unusual & rare materials for their art",
14: "Explore the world to better portray it",
15: "Complete a cycle of the monsters they kill",
16: "Desperately trying to overcome a block",
17: "Prove themselves worthy to the muses",
18: "Art is transformative, so is violence",
19: "Prove they're not a sellout but a true artist",
20: "Have their art reach other realms & planes",
}
artist_catalysts = {1: "Decides their life should be the work of art",
2: "A wealthy & powerful patron ropes them in",
3: "Tasked to capture a legendary location",
4: "A work creates an unexpected controversy",
5: "The spirit of an ancient artist reaches out",
6: "A promising young ingénue asks for help",
7: "A famous piece contains hidden secrets",
8: "Spirits of creation send visionary dreams",
9: "A colleague suggests a collaboration",
10: "A piece of theirs suddenly gains sentience",
11: "A fan finds unintended meaning in their art",
12: "An artistic hero tasks them to be a hero too",
}
artist_growth = {1: "From starving artist, to rich and famous",
2: "Creatively blocked, to feeling the flow state",
3: "Focused only on product, to enjoying process",
4: "Evolution in artistic style mirroring their growth",
5: "Healing trauma by turning it into art",
6: "Self-centered, to making a societal impact",
7: "Aspirational, to masterful, to transcendent",
8: "Student of a craft, to inspiring a new generation",
}
artist_friends = {1: "Dreamweavers: Traveling, rotating exhibition mixing multiple medias with illusory magic",
2: "The Writing on the Wall: Secretive affiliation installing works by night that question authority",
3: "Family of Light and Color: Guild of painters that spread to other arts, throws great parties",
4: "Cosmic Choir: Some believe they are interpreting & influencing music of the spheres",
}
artist_assets = {1: "Cedric Vonclair: Flamboyant collector who loves juicy rumors even more than he loves art",
2: "Elotine Thornfield: Kind noble and bad poet who supports artists with her social connections",
3: "Elysia: Enchanting and mercurial fey spirit who is a retired muse but still has her magic",
4: "Professor Henrietta Dailey: Art historian with extensive knowledge on many subjects",
5: "Brundt Gunderson: Prolific sculptor with a background in architecture, mining, & quarries",
6: "Rodigo Martez: Retired adventure who paints landscapes, drinks tea, and tells stories",
}
artist_items = {1: "A folded sketch made by someone very significant from the Artist's past",
2: "A cherished childhood toy that inspired their earliest creative works",
3: "Honesty Quill: Can only draw or write truth and blots out inaccuracies and lies",
4: "Illusory Palette: Painted objects become three dimensional with mass of paper machete",
5: "Sculptor's Diamond Chisel: Cuts through stone like wood, but it is noisy & takes time",
6: "Chameleon Canvas: The figures painted on it shift to reflect the closest viewer's emotions",
7: "Choreographers Block: Once per day can compel those in range to dance for 1 minute",
8: "Acme Brush: A door painted with this becomes real, but only for a short time",
9: "Harmonic Flute: Attuned user can play resonant frequency to cause an object to float",
10: "Enchanted Craft: Glaze that can animate piece of art for one hour when applied",
}
artist_antagonists = {1: "Forger's Emporium: A network of greedy counterfeiters whose work is devaluing real art",
2: "Iconoclastics: A cult who believes only the gods can create beauty and so destroy artwork",
3: "The Art Department: Propaganda wing of an evil empire spreading lies through murals",
4: "Order of Purity: Believe too much color & most art triggers evil thoughts in the populace",
5: "People's League: Destroys the works of other cultures to uphold a feeling of superiority",
6: "The Recollectors: Former adventurers who found stealing art more lucrative & much safer",}
artist_rivals = {1: "The Marble Gardens: Sculpture collection that is actually petrified creatures & humanoids",
2: "Divine Gallery: A secluded temple adorned with prophetic frescoes that change over time",
3: "Illusory Ruins: Crumbling fey court castle where ghosts entrap any who enter with beauty",
4: "Chromatic Cliffs: The wind sings passing over the stone & waterfalls create rainbows",
5: "Dark Salon: The subjects of these lifelike paintings are magically bound within the canvas",
6: "The Giant's Pipe: Massive ocarina that can open doors or summon monsters when played",
}
artist_locs = {1: "Bella Nocturne: Weaving enchantment magic into her work is the key to her success",
2: "Sillip Crocket: Since childhood has told the artist they will never amount to anything",
3: "The Splasher: Unknown person defacing and destroying works of art around the city",
4: "Seraphina Scribeheart: Harsh critic who believes nothing compares to the ancient works",
5: "Kalthazar: A doppleganger who has been impersonating artists & hurting their reputations",
6: "Darius Kindler: Stifled creative ambitions have warped into destructive love of arson",}
artist_monsters = {1: "Drab Wrath: A being of shadows that drains color, sound, and life energy wherever it goes",
2: "Graffiti Gargoyle: A winged statue animated to stop vandalism in an ancient magocracy",
3: "Symphonic Sprites: Live inside instruments and can inspire brilliance or madness",
4: "Marble Guardians: Sculpted of celestial stone, they patrol long empty temple halls",
5: "The Painted Lady: A hag shrouded in illusion who paints horrors that leap off the canvas",
6: "Entangling Tapestry: Heavy wall hangings that wrap around and smother trespassers",
}
artist_plot_hooks = {
1: "The location of an ancient master's studio is uncovered to be in a remote and dangerous locale",
2: "Obtain rare materials for an art competition with incredibly high stakes",
3: "Missing artworks point to a criminal enterprise with a political agenda",
4: "Someone or something is replacing art pieces with forgeries & mimics for unknown ends",
5: "The walls of an newly discovered archaeological site seem to depict an impending disaster",
6: "A composer has crafted an opus that if played perfectly opens a portal to another plane",
7: "A tyrannical abomination is only placated by works of beauty to contemplate",
8: "Ancient cave paintings give clues to a forgotten lineage of an ancient druidic circle",
9: "A cursed painting is up for auction, it's previous owners have all met horrible ends",
10: "An otherworldly judge demands proof this culture produces worthy art and deserves to continue",
11: "There's a lucrative commission to capture the likeness of a reclusive monster thought to be myth",
12: "Brain-eating monstrosities from the underworld have found creative minds are extra delectable",
13: "A masterwork of a fallen civilization has been uncovered, seeming to trigger unusual events",
14: "Resonant patterns from the vibrations of a specific melody are the key to unlocking a sacred seal",
15: "A remote retreat preserves a lost art form capable of summoning celestials, demons, & devils",
16: "The nobility are paying exorbitant prices for authentic landscape paintings of dungeons",
17: "An illustrated book of children's rhymes long thought to be mere fairy tales turns out to be truth",
18: "Vampires have begun enthralling portrait artists since they can't see their own reflections",
19: "An immersive art experience is secretly a ritual a cult is performing to funnel power to their deity",
20: "Reproductions have ignited a passion for authentic ancient works and a dungeoneering gold rush",}

barkeep_drives = {1: "Experience what they've only heard in story",
2: "Find locations and funds to expand business",
3: "Discover new recipes and ingredients",
4: "Have adventures before they settle down",
5: "Extend safe inclusiveness beyond their walls",
6: "Earn the respect of adventuring patrons",
7: "Collect artifacts to decorate their tavern",
8: "Gain widespread renown to promote the bar",
9: "Carry on the family legacy and tradition",
10: "Explore the world waiting beyond their limits",
11: "Learn from various other establishments",
12: "Transform the inn to something much more",
13: "Obtain enough wealth to not lose business",
14: "Source exotic concoctions and brews",
15: "Secure peace to ensure travel and trade",
16: "Get monster's head for the best tavern sign",
17: "Grow strong to better protect their inn",
18: "Have a signature drink named for them",
19: "Get rich so they can buy their own place",
20: "Inspire a song to be played at bars for ages",}
barkeep_catalysts = {1: "The inn was built atop an ancient ruin",
2: "Grandad's trunk in the cellar holds a secret",
3: "A tavern brawl has rippling consequences",
4: "The best rumors are at the bottom of a bottle",
5: "A long-time patron is not what they seem",
6: "A magic-fueled monopoly threatens business",
7: "A wager or a bad deal costs them the bar",
8: "Travelers tell tall tales, some are even true",
9: "A retired adventurer wants a job to stay busy",
10: "Someone pays their tab with a magical item",
11: "A map is carved into the wood of a table",
12: "Bard shares a song they don't sing on stage",}
barkeep_growth = {1: "Earning income, to providing refuge",
2: "Stuck in one place, to seeing the world",
3: "Transforming the tavern to a community hub",
4: "Poor and struggling server, to incredible tipper",
5: "Micromanaging, to trusting others",
6: "Story collector, to storyteller, to story subject",
7: "Obsequious people pleaser, to very confident",
8: "Humblest beginnings, to heroic figure",}
barkeep_friends = {1: "The Circuit: A loose affiliation of bards and other traveling acts who share info and news",
2: "The Crawlers: Dungeoneers who spend their time in various taverns, until the gold runs out",
3: "Hoptimists: Druids building good will with settlements by trading their wild yeast brews",
4: "Wayfarer's Guild: Create and update guides for travelers, especially gold-laden adventurers",}
barkeep_assets = {1: "Tusks and Knucks: Punch-drunk bouncer twins who were once muscle for a thieves guild",
2: "Benton Gegor: Town guard who calls time at the bar while on duty “community policing”",
3: "Islode Glint: Glassblower who makes drink ware, also vessels for herbalists and alchemists",
4: "Tibs: Disguised nymph on the run from realm of fey, mediocre waitress but a big draw with patrons",
5: "Masked Mandolin: Mysterious troubadour with knowledge and stories of faraway lands",
6: "Brother Farby: Monk from nearby monastery who enjoys talking about brewing methods",}
barkeep_items = {1: "Tattered piece of parchment with a well-loved and carefully guarded family recipe",
2: "A bottle of a rare and expensive vintage, saved for a special occasion (or a rainy day)",
3: "Rag of Resilience: Can magically clean most surfaces, and absorb 10 cubic feet of water",
4: "Dog Hair Potion: Removes drunkenness, hangovers and the effects of minor poisons",
5: "Hearthstone: Smooth rock that is always warm and gently pulls toward home",
6: "Crystalline Pint: Purifies anything poured into it, removing poison and disease",
7: "Tankard of Tongues: Drinking from this grants fluency in one language for one hour",
8: "Apron of Accessibility: Has a pair of extradimensional pockets,keeping items handy",
9: "Veritas Vinos: It is impossible to lie for ten minutes after drinking from this vessel",
10: "Tapster's Key: Opens portal to extra-dimensional inn with room and board for 100",}
barkeep_antagonists = {1: "Town Council: Corrupt officials who demand frequent bribes from local businesses",
2: "The Busted Barrel: Rival tavern run as a front by thieves guild, doesn't love competition",
3: "Gutter Rats: Petty criminals who frequent the bar but mostly stay out of trouble there",
4: "Nephalists: Small sect of teetotalers who want all bars closed and alcohol criminalized",
5: "Iron Cartwheel: Caravaners manipulating routes and markets through nefarious means",
6: "Eavesdroppers: Spy network for hire that listens in at tables and private rooms in taverns",}
barkeep_rivals = {1: "Labyrinthine network of tunnels utilized by moonshiners, bootleggers, and other creatures",
2: "The Cyclopean Ruins: recently discovered while expanding the tavern's cellar",
3: "Purple Stills: A distillery turned mad alchemist's laboratory, filled with volatile chemicals",
4: "House of Spirits: Haunted ruins of a monastery who loved drinking over their gods",
5: "The Swuare: Bustling market square where the tavern acquires most of its supplies",
6: "The Crossroad:s near the inn where it is said one can make a deal with a devil at midnight",}
barkeep_locs = {1: "Billiam “Rickets:” Town drunk, begs patrons to buy him drinks for his (mostly false) stories",
2: "Garmund Frith: Collects the taxes on sales of alcohol, widely hated and likes it that way",
3: "Oswalt Wulfson: Notorious bully who enjoys starting brawls, secretly cursed with lycanthropy",
4: "Ailla Cane: Aspiring leader of a cult to a god of elemental chaos, hand writes pamphlets",
5: "“Bitters” Augustino: Spreads the rumor his family recipe was stolen by character",
6: "“Cutthroat” Eucher: Crafty gambler with an ace up his sleeve and a dirk at his belt",}
barkeep_monsters = {1: "Rat King: A swarm of giant rats with their tails knotted together, mostly acting as a one",
2: "Wort Hog: Stinking peccaries that are attracted by the smells of the brewing process",
3: "Cask Mimic: Typically disguised as kegs and barrels, young ones imitate jugs and flasks",
4: "Hop Blights: Plant monsters that try to vine around and intoxicate their targets",
5: "Growlers: Tiny imps that enjoy the liquor absorbed by the wood of casks",
6: "Drunken Djinn: Powerful air elemental sealed in a liquor bottle by a humorous wizard",}
barkeep_plot_hooks = {1: "A bottle of a particular vintage must be tracked down and delivered to christen the new royal ship",
2: "Rediscover a lost recipe believed to show fermentation was the key to a potion-making process",
3: "A divine being of hospitality requires help in extending safety and security in a dangerous land",
4: "One of the regulars, always an excellent tipper, has gone missing under mysterious circumstances",
5: "The road must be made safe again from bandits or travelers will never return to the tavern",
6: "Renovations have uncovered a disturbing secret long hidden behind the tavern's walls",
7: "A monstrous incursion in the countryside threatens the inn's ongoing supplies, and its suppliers",
8: "After losing half of their group in a dungeon, a party limps in and swears off the adventuring life",
9: "The curse is spreading, the mayor may be complicit, and if this continues the whole town will fall",
10: "After renting a room last night, a patron left some sort of egg behind and now it's about to hatch",
11: "The mirror behind the bar is not showing a reflection of this room, but a different scene entirely",
12: "The mythical beast that adorns the tavern's sign suddenly makes an appearance",
13: "A clandestine group has chosen the bar for their secretive rendezvous, but the word got out",
14: "It turns out the bard's new song is much more than it seemed at first",
15: "They've been at their usual table most nights, so discovering they died months ago was shocking",
16: "The rival factions have always considered the tavern neutral ground, but that truce has broken",
17: "An inebriated patron confesses to a secret that could plunge the whole empire into civil war",
18: "The hoard of evil marauders thought the tavern made a juicy (and flammable) target",
19: "It was a quiet night until she burst through the door, wide-eyed and breathlessly begging for help",
20: "The job board was just a way to bring in more business, but quests went up beside the odd jobs",}

barrister_drives = {1: "Continue the family tradition of lawyers",
2: "Balance the scales in favor of justice",
3: "Protect the weak who need representation",
4: "Pay off the huge debt from their education",
5: "Expose the corruption in the power structure",
6: "Prove that no one is above the law",
7: "Redeem themselves for past inequities",
8: "Seek just revenge for a wrong done to them",
9: "Spread law and order to lawless lands",
10: "Be recognized as the greatest legal mind",
11: "Overturn a long-standing, unjust law",
12: "Embody the divine justice of their god",
13: "Codify a legal system across the species",
14: "Reform the current, flawed penal system",
15: "Clean up the criminal underworld",
16: "The truth shall set you free, or incriminate",
17: "Winning arguments is a thrill in its own right",
18: "The worlds not fair but we can make it so",
19: "Violence begins where debate ends",
20: "Harsh punitive measure prevent worse evils",}
barrister_catalysts = {1: "Parental figures wanted kid to be a lawyer",
2: "Law books were their only company for years",
3: "A traumatic injustice formed their worldview",
4: "Fascinated by court's gravitas and drama",
5: "Did crime, served time, turned over new leaf",
6: "A chance encounter with a wise, kindly judge",
7: "Father figure made a deal with the devil",
8: "Realm's in legal chaos over next successor",
9: "Corrupt shire-reeve destroyed their business",
10: "Retired knight who traded sword for pen",
11: "Wrongfully accused of another's crime",
12: "Legal loopholes cost them their birthright",}
barrister_growth = {1: "Law-abiding citizen, to extralegal vigilante",
2: "Upholding tradition, to progressive reformer",
3: "Local disputes, to the highest courts in realm",
4: "Lawful neutral, to neutral good",
5: "Arguing & advocating, to judge & lawmaker",
6: "Focus shift from getting paid to greater good",
7: "From exploiting loopholes, to closing them",
8: "Fulfilling vendettas, to upholding true justice",}
barrister_friends = {1: "Tipsy Scales: Seasoned justices who like to talk about their cases & play drinking games",
2: "Parchment House: Bureaucratic institution keeping meticulous legal records for centuries",
3: "Canary Choir: Undercover operatives who infiltrate criminal organizations",
4: "Brass Button Agency: Private Investigators with a diviner on staff, not cheap but effective",}
barrister_assets = {1: "Brother Merci: Cleric serving the poorest fringes of society, has friends in low places",
2: "Wanda Quillhart: Incredibly fast scribe, who records notes for the highest cases & meetings",
3: "Sir Galen: Retired knight who traded his sword for the pen to continue perusing justice",
4: "Whittaker Silver “Tongue”: Technically a rival in court but operates with decorum & respect",
5: "Bruna Veritas: No nonsense judge who does the right thing but doubts anyone else ever will",
6: "Carthrash: Bouncer turned bailiff with more tattoos than teeth & an oft underestimated mind",}
barrister_items = {1: "A worn, ancient badge from a legendary lawful order who were judge, jury, & executioner",
2: "A letter in a shaky hand from a grateful client, dictated to their child who could write",
3: "Inkwell of Revelation: False words come out a different color if the writer knows they're lies",
4: "Robes of Oration: Lend an air of authority and improves ability to persuade non-hostiles",
5: "Gavel of Judgment: When activated, magically grows into a +1 warhammer",
6: "Justices Reach: 10' whip that can grapple, pull, and knock prone in one attack motion",
7: "Oath Binder Tome: Swearing on this causes psychic damage if they go back on their word",
8: "Scroll of Summons: Can summon anyone on the same plane if their true, full name is known",
9: "Amulet of Objection: Allows for an extra reaction interrupting enemy turn once per day",
10: "Rings of Binding: When two parties shake while wearing, both will know if a deal is broken ",}
barrister_antagonists = {1: "Quiet Council: Local political influencers who uphold a flawed status quo which benefits them",
2: "Angels of Anarchy: Outlaws who project a romantic life of crime but commit evil often",
3: "Blood Pact: Devil worshipers deceiving people into signing contracts with their patron",
4: "Noblesse Oblige: Debaucherous aristocrats who believe that laws are only for commoners",
5: "The Watch: Draconian guards who much rather punish innocents than let guilty go free",
6: "The Silvered Nib: Network of forgers for hire, known to counterfeit evidence among other jobs",}
barrister_rivals = {1: "Scales of Justice: Pair of balanced platforms that rise and fall under weight, unknown origins",
2: "Celestial Court: Dimension where a deity judges the worthiness of their follower's souls",
3: "Jurat Abbey: Lawful good monastery where disputes are heard and settled for a donation",
4: "The Forum: Tiered sunken amphitheater where public debates and trials are held",
5: "Justice Square: Plaza with gallows and guillotine where executions are performed",
6: "Penal Pit: Ancient prison complex bored deep into the earth, abandoned to the inmates",}
barrister_locs = {1: "Silas Ashe Esquire: Charges wealthy clients exorbitant fees to bend the law in their favor",
2: "“Chubs” Goldfab: Runs local thieves guild, has standing vendetta against all lawyer types",
3: "Shem Griswold: An “informant” who fabricates most of what he claims to witness",
4: "Akamo Wenta: Well-known fence, magic items they sell have been known to go missing",
5: "Rhys Lewyn: Constable whose power has gone to their head, and lines their pockets",
6: "Grace Westwood: Aspiring performer who accepted a well-paying role as a false witness",}
barrister_monsters = {1: "Parchment Wraith: Magically animated documents that slash with paper cuts",
2: "Jolgoth the Corrupter: Mid-level demon who enjoys subverting those who uphold the law",
3: "Slanderous Serpents: Shape-shifting snake folk, impersonate others to lie, steal, or kill",
4: "Tozen the Litigious: A mage whose gained power by making contracts with dark forces",
5: "Chaos Goblins: Wield blades with their prehensile tails and abhor all forms of order",
6: "Judgernaut: Construct enforcing ancient law criminalizing people who get too powerful ",}
barrister_plot_hooks = {1: "A group of “monsters” are seeking their rights in the eyes of the law as they defend their territory",
2: "An evil cult has secretly infiltrated and undermined the settlement's seats of power",
3: "A tyrant has outlawed all sources and practitioners of magic, fearing it threatens their authority",
4: "A recently escaped criminal is getting revenge by blinding anyone connected to the justice system",
5: "A recently uncovered ancient law has called the ruler's claim into question and created turmoil",
6: "Minor infractions are being invented to imprison the populace and force them into labor camps",
7: "In a land where the only punishment is fines, the rich elite can literally get away with murder",
8: "Witnesses have been intimidated into silence to prevent a general panic among the commoners",
9: "The party has been framed for a crime and the best defense is finding the true perpetrator",
10: "The poison sets in before the would-be whistle-blower can share all of their insider information",
11: "The state legally claims all bodies after death, fielding a tireless undead workforce and military",
12: "The mages have implemented new surveillance “to prevent crime,” not even thoughts are private",
13: "The dragon is way too powerful to defeat with force, but it is ready and willing to negotiate",
14: "Even if defeated in battle, the incorporeal spirits will keep returning until they receive justice",
15: "The incursions from Hell will only stop when the ancient agreement is rediscovered and honored",
16: "The monstrous tribes have their own laws and customs, however chaotic they seem to be",
17: "A powerful Sphinx requires everyone in their domain to follow strictly enforced byzantine laws",
18: "A sorcerer is taking advantage of legal loopholes that allow enslaving creatures from other planes",
19: "The law of the land allows trial by combat, the defendant and accuser can choose champions",
20: "A confusing agreement with fey has caused the kingdom to plunge into colorful, dangerous chaos",}

bounty_hunter_drives = {1: "Become a well-known legend in their time",
2: "Get rich quick whatever the risk",
3: "Nothing matches the thrill of the chase",
4: "Give targets one last chance at redemption",
5: "Provide sacrifices to satisfy god of death",
6: "Seeking to make up for their criminal past",
7: "Improving their skills to one day get revenge",
8: "The justice system failed them, never again",
9: "Prove their worth after being underestimated",
10: "Stand up for those who need help",
11: "Earn enough to reclaim the ancestral land",
12: "“Collect” various types of folk and creatures",
13: "Fill the bounty of a love who wronged them",
14: "Actions have consequences, and it's them",
15: "A hero gotta have a code",
16: "They could retire, but just one more score",
17: "They can bring others peace, so they must",
18: "Live up to the legacy of their mentor",
19: "Pay off a loved one's crippling debt",
20: "Loves killing monsters, may as well get paid",}
bounty_hunter_catalysts = {1: "Brush with a criminal changes them forever",
2: "Corrupt authorities, better to act alone",
3: "A longtime fascination with wanted posters",
4: "A parental figure has a price on their head",
5: "There's been a case of mistaken identity",
6: "Trade is passed down through generations",
7: "Trained as assassin, wanted to do good",
8: "Personal vendetta that launched a career",
9: "Tracks missing persons after personal loss",
10: "Cursed to kill, but makes the best of it",
11: "Subsistence hunter turned to bigger game",
12: "There's always the one that got away",}
bounty_hunter_growth = {1: "Single-minded revenge, to nuanced justice",
2: "Lone wolf, to a valuable part of the team",
3: "Broke and fringe, to celebrated philanthropist",
4: "Mixed reputation, to honored and celebrated",
5: "From working harder, to working smarter",
6: "Cold and ruthless, to unlocking empathy",
7: "No attachments, to loving relationships",
8: "Only out for self, to making the world safer",}
bounty_hunter_friends = {1: "Arcane Eyes: Practitioners of divination, expensive with no guarantees, but often useful",
2: "Big Shots: Bards and criers sharing the latest news on captures, crimes, and bounties",
3: "Queen's Quiver: Originally monster hunters, now talks more theory than actually practices",
4: "Fox Den: Criminals with a code of conduct, place bounties on members who break it",}
bounty_hunter_assets = {1: "Leon: Retired hit man with traps and weapons stashed all over his home and garden",
2: "Stew Lee: Petty criminal with no stomach for violence, his main trade is selling information",
3: "Amabel Swann: Sketch artist, makes wanted posters and illustrations for exotic bestiaries",
4: "“Waltzing” Matilda: Talented beginner who enjoys “the dance” of tracking bounties",
5: "Masiko Pound: Breeds and trains tracking hounds, prefers dogs to people",
6: "Dawa Ang: Antiques dealer with connections to, and rumors from, all levels of society",}
bounty_hunter_items = {1: "The tattered and stained wanted poster from their first job as a bounty hunter",
2: "A dagger a target once embedded in their thigh, so they always remember",
3: "Lens of Tracking: Helps footprints and trails stand out in higher contrast",
4: "Cloak of Camouflage: Appearance adapts to the environment to make stealth easier",
5: "Spellslinger Shackles: When locked in place prevent casters from using most spells",
6: "Wondrous Lasso: Casts golden light as torch, restrained creatures can only speak truth",
7: "Veil of Vision: Transparent face covering that allows wearer to see through illusions",
8: "Cuffs of Compliance: When locked, wearer is more susceptible to enchantment and charms",
9: "Cold Iron Compass: Points to a named person or creature if within 1,000 feet of target",
10: "Spectral Snare: Reusable trap that restrains target when triggered, invisible when armed",}
bounty_hunter_antagonists = {1: "Brickyard Crew: Dimwitted thugs, rudderless since leader fled with a bounty on their head",
2: "Web of the Spider: Shady spy network that recruits urchins, barkeeps, and other informants",
3: "The Watch: Lazy and ineffectual local guards who resent being shown up by outsiders",
4: "A Glint in the Shadows: Secret network of assassins for hire who specialize in poisons",
5: "The Consortium: Wealthy merchants whose white-collar crimes will never be investigated",
6: "Iron Collars: Unscrupulous bounty hunters rumored to secretly be slavers as well",}
bounty_hunter_rivals = {1: "The Shattered Smile: Small island chain known to harbor criminals and pirates",
2: "Sepia Sands: A vast desert dotted with mineral deposits and lawless towns",
3: "The Buoyant Bazaar: Mobile flotilla of vendors trading all types of goods of stories",
4: "The Sanctuary: Secret temple to the god of thievery that's fleecing followers of other faiths",
5: "Underside: Patchwork district of the city made of labyrinthine sewers, cellars, and caves",
6: "The Blackwood: Unexplored forest filled with giant beasts, monstrosities and a bandit camp",}
bounty_hunter_locs = {1: "Chappy “Big Dog” Vulf: Flashy braggart who snipes bounties by following other hunters",
2: "Arman “The Serpent” Hrach: Crime lord with an open bounty on heroes and hunters",
3: "“Bloody” Bartholomew: Ruined reputation by returning as undead after bounty was collected",
4: "Lady Wagombe: Heiress with a grudge after her brother was hit by an errant crossbow bolt",
5: "Xola Shadowfoot: A former tracker turned thief her skills and knowledge to evade capture",
6: "Thane Jargutha: Warlord with a bounty on the head of everyone who's put a bounty on his",
}
bounty_hunter_monsters = {1: "Reverent: Undead vigilante with no scruples killing innocents to reach targets for its revenge",
2: "Doppelganger: Shape-shifts into others' forms to frame them for crimes it commits",
3: "The Slaver Drake: Dragon who sends its minions out to capture slaves to serve it",
4: "Cerberus: Demonic three-headed hound that can track the blood scent on any who've killed",
5: "Nightstalker: Creatures summoned from shadow realm who crave to hunts the hunters",
6: "Pit Ghasts: Fugitives from Hell, use the glowing hot chains that bind them as weapons",}
bounty_hunter_plot_hooks = {1: "The quarry put a bounty on themselves to distinguish the finest trackers for their own task",
2: "The people posting bounties are turning up dead, robbed of the reward money",
3: "A criminal surrenders in order to be brought in, fearing for their life from something worse",
4: "Someone has put a price on the heroes' heads and various adversaries will keep coming to collect",
5: "A wealthy patron is hiring to track down a relative who decided to try their hand at adventuring",
6: "The clues point to the target hiding out in the nearby dungeon where they think none will follow",
7: "A mage puts a list of bounties up on rare creatures, requiring different parts of them for alchemy",
8: "The fugitive always returns to their home town for the festival, but will be disguised",
9: "Convinced their last collar was a patsy they are encouraged to now break them out of prison",
10: "The mayor's offering a huge reward but the target is actually a whistle-blower revealing corruption",
11: "A bored and reckless noble will pay to be taken on a real adventure, as long as they survive it",
12: "The bounty has been increased four times, once for each party the monster's defeated",
13: "The target offers to double the bounty on its head if allowed to go free and continue its evil plan",
14: "Crude spelling and drawing on the orc clan chief's wanted poster reveals it was made by goblins",
15: "A fugitive insists they're innocent and promises a huge reward if the party can prove it",
16: "Someone's resurrected the last threat the party took out, now it's stronger and wants revenge",
17: "A mastermind is paying for the capture of targets in order to recruit them and build their team",
18: "Unusually, a bounty has been placed on an item, which might be more valuable than the reward",
19: "No one knows the quarry is possessed by a curse, which will find a new host if this one is killed",
20: "The target must be convinced to leave on their own, killing or capture will mean big consequences",}

charlatan_drives = {1: "Protect the secret of their true identity",
2: "Become the person they pretend to be",
3: "Achieve fame without being truly known",
4: "Avoid detection by their old associates",
5: "Gather wealth for family they're ashamed of",
6: "Reinvent themselves to win an old flame",
7: "Prove they can outsmart everyone",
8: "Escape their past because it was traumatic",
9: "Reinvent their past because it was boring",
10: "Lie so well it actually becomes the truth",
11: "To one-up themself in their personal game",
12: "Deceive the very gods themselves",
13: "Orchestrate an epic con to get revenge",
14: "Freedom in personal reinvention",
15: "Craft a mythic persona worthy of song",
16: "Hide the fact their identity has been lost",
17: "Terror at idea of simply being ordinary",
18: "Life can be whatever we want it to be",
19: "This alter ego allows them to be brave",
20: "Everyone is fake, they're just honest about it",}
charlatan_catalysts = {1: "They conned the wrong person in the past",
2: "A small deception that snowballed over time",
3: "Learned the “family business” at young age",
4: "Fooled once, now they will never be again",
5: "Pushed into a witness protection scenario",
6: "Can't live with who they really are",
7: "Heir apparent but wanted to go own way",
8: "Heir apparent and hunted because of it",
9: "Blamed for a crime and now a fugitive",
10: "Lost love, reinvented self to be appealing",
11: "Could no longer live with “true” self",
12: "Inspired by heroes with secret identities",}
charlatan_growth = {1: "Complete denial, to honesty with self",
2: "Frog to prince style revelation,. or the other way",
3: "Truly becoming what they've pretended to be",
4: "Opening the circle and let others in on secret",
5: "Conning for profit, to doing it for greater good",
6: "Reckoning with and integrate their past identity",
7: "From lies and disguise, to enchanting illusions",
8: "Protected by lies, to honest vulnerability",}
charlatan_friends = {1: "Farcical Mummers: Performing troop who excel at embodying roles and stage makeup",
2: "The Velvet Venue: Tavern where con artists, fences, and brokers of secrets meet and mingle",
3: "Scullery Society: Servants guild who gossip about their employers' wealth and propensities",
4: "The Wanderers: Touring musicians happy to share travel stories, some of them are even true",}
charlatan_assets = {1: "Nester Bem: Pawn broker who doesn't ask questions, has an eye for fakes and curses",
2: "“Honey” Pots: Her love-besotted marks rarely know, or care, that they've been conned",
3: "Brother Puck: Disguised satyr hiding out in a monastery to avoid fey court and corrupt monks",
4: "Tansy Sabine: Young street urchin who knows many secrets of the city",
5: "Reginald Worrel: Well-connected aristocrat whose true origins are far from noble",
6: "Morag Yon: A bookie who will set a line on just about anything and loves a good fix",}
charlatan_items = {1: "Lucky Coin: Weighted so that it always lands heads down when flipped",
2: "Locket with a portrait from the past whose true significance is a closely guarded secret",
3: "Silver Tongue Tincture: Potion that grants a benefit to persuasiveness for one hour",
4: "Face Eraser: Magical mask that instantly disguises the wearer's appearance at will",
5: "Cloak of Concealment: Reversible cloak that can turn wearer invisible for ten minutes",
6: "Fool's Gold: Transmutes any metal to gold for one day, effect can be detected as magic",
7: "Chalice of Charm: Drinking from this cup renders one more susceptible to enchantments",
8: "Adaptable Wax: Mimics seals, aids in forgery and resealing opened missives undetected",
9: "Ring of Reputability: Aids wearer in all attempts at deception",
10: "Shades of Subtlety: Dark glasses that penalize perception but increase insight ",}
charlatan_antagonists = {1: "The King's Seekers: Investigating knights perusing “justice” in the name of long dead king",
2: "Seering Light: Overzealous sun god worshipers who hate all forms of deceit",
3: "Market Watch: Brash mercenaries hired by merchant's guild to patrol commercial districts",
4: "The Black Envelope: Criminal network that specializes in espionage and extortion",
5: "The Flimflam Band: Amateur cons whose halfbaked schemes keep others on their guard",
6: "Griffin Roost: High society social club filled with inherited wealth to dupe elites out of",}
charlatan_rivals = {1: "Manse of the Masquerade: Sprawling manor that hosts masked balls full of intrigue",
2: "The Crooked Spire: Ruined wizard's tower filled with illusions and trapped false floors",
3: "House of Mirrors: Mysterious temple where alternate versions of the self can be glimpsed",
4: "Badger's Den: Popular underground gambling hall run by the eponymous Badger",
5: "Citadel of Shadows: Ruins where you could lose your shadow, sense of self, and very soul",
6: "Moonlit Carnival: Traveling Circus where everything is magic and very little is as it seems",}
charlatan_locs = {1: "Broderick the Righteous: Would-be paladin with a personal vendetta after being fooled",
2: "Rivers Turner: Runs crooked card games and resents anyone else deceiving marks",
3: "The Vindicator: Masked bounty hunter who blurs the line between vigilante and assassin",
4: "Trish “Clarity” Clearwater: Retired con artist who grew bored and now targets other cons",
5: "Bellamy Cog: Honest member of the watch who can smell a liar from a mile away",
6: "Moon-eyed Magdula: Fortune teller giving fake readings, mixed with flashes of true divination",}
charlatan_monsters = {1: "Tricksies: Winged fey sprites who love of pranking big folk borders on harassment",
2: "Mimics: Iconic monsters famous for pretending to be something else",
3: "Hags: Traditionally derive pleasure from causing suffering through acts of deceit",
4: "Doppelgangers: Can change their looks to impersonate others and steal identities",
5: "Changeling: Human-like monster secretly left in place of a stolen child",
6: "Sphinx: Dispel illusions and difficult to fool, posses riddles to get past it alive ",}
charlatan_plot_hooks = {
1: "A magic item hanging in a noble family's home must be taken, it's best if they don't know it's gone",
2: "A figure who knows secrets from the past arrives and threatens to reveal their true identity",
3: "A false prophet claims the world is ending, convincing followers to give up all of their possessions",
4: "The map to a famous con artist's treasure is discovered, but it may just be an elaborate ruse",
5: "Someone must impersonate a foreign emissary to prevent the outbreak of war",
6: "Rumors are circulating about them, not their persona but the real them, it must be an impersonator",
7: "A noble will pay well for a double to act as a trap to lure out the assassins out to get them",
8: "Evidence has been planted at a heist to frame them for a crime they did not commit",
9: "A friend has gotten themselves in way over their heads and sends a desperate plea for help",
10: "A cult is creating a tremendous zone of truth and without white lies the town will soon destroy itself",
11: "It will be difficult to deceive the dragon but defeating it in direct combat is not a possibility",
12: "To gain access to the catacombs they'll have to fake their own death, getting out is the hard part",
13: "To inform the queen of the coming peril they'll need to infiltrate the court one way or another",
14: "A self-made merchant baron offers a large reward to bury a threatening specter from their past",
15: "This new faith may be an elaborate divine con job with devilish origins",
16: "The target is not what it seems but is actually possessed by a sentient magical weapon",
17: "To gain access to the criminal kingpin they'll first have to gain the thieves guilds trust",
18: "Locals are going missing, coming back to behave oddly and claim no memory of what happened",
19: "The only way to prevent the heist of the century is to steal the McGuffin themselves",
20: "An old friend is discovered living under a new name, they have a story and a potential quest",}

cook_drives = {1: "Discover new recipes and exotic flavors",
2: "Earn a fortune to fund their own restaurant",
3: "Create peace so people can enjoy their food",
4: "Prepare a meal worthy of the gods",
5: "Preserve the food culture of a lost civilization",
6: "Gain fame and start a cooking competition",
7: "Compile the greatest cookbook in history",
8: "Find easier life than long hours in the kitchen",
9: "Prove the worth of their lowly profession",
10: "Gather rare ingredients from far away lands",
11: "Have a dish named after them",
12: "Establish an innovative culinary school",
13: "Ensure that no one ever goes hungry",
14: "Good food can bring people together",
15: "Cook for the rich, powerful, and mythical",
16: "Food is medicine for body, mind, and soul",
17: "Violence is just the prep work for peace",
18: "Elevate cooking to the level of art or magic",
19: "Infuse the world with more hospitality",
20: "They live to cook, and they kill to live",}
cook_catalysts = {1: "A map written on the back of a recipe",
2: "A poisoner sabotaged their reputation",
3: "Spice traders bring news from far away",
4: "A mentor reveals they weren't always a cook",
5: "The rumored source of a rare ingredient",
6: "Secrets overheard catering a noble banquet",
7: "A dishwasher on the run from their past",
8: "Conjured food is disrupting the profession",
9: "Notes left in the margins of an old cookbook",
10: "Whispers swirl among the vendors' stalls",
11: "A spicy dish causes visionary dreams",
12: "It's said an army marches on its stomach",}
cook_growth = {1: "Lowly kitchen help, to well-renowned legend",
2: "Rigid pursuit of perfection, to pursuit of joy",
3: "Overcoming a fear of criticism and reviews",
4: "Achieving balance, in dishes, and in life",
5: "Overly competitive, to cooperative member",
6: "Gaining respect of world that undervalues them",
7: "Broadening horizons beyond the kitchen",
8: "Chasing extravagance, to appreciating simplicity",}
cook_friends = {1: "The Flavor Flow: Spice merchants with ingredients and rumors from many lands",
2: "Movable Feast: Throw lavish dinner parties with expensive tickets and elite guest lists",
3: "Daily Bread: Religious sect that feeds those in need as an act of devotion to their deity",
4: "The Taste Buds: Food critics that rate and review taverns and publish travel guides",}
cook_assets = {1: "Chef Jeff: One of the best, when he's sober., who once worked for the highest in the land",
2: "“Damascus” Griggs: Smith with the strongest and sharpest knives, and other bladed weapons",
3: "Red Hostler: Tavern keeper with a willingness to experiment with their menu",
4: "Carlyx the Risen: Studies all types of fermentation with nearly religious fervor",
5: "Gaston: A ghost with knowledge from the past who envies the living's ability to enjoy food",
6: "Obazu Ren: Hunter who provides rare game meats and is at home in the surrounding wilds",}
cook_items = {1: "A family recipe that represents generations worth of tradition and heritage",
2: "A metal on a blue ribbon denoting first prize in a cooking competition",
3: "Magically Soluble Goodness: Renders any food delicious and invokes cravings for more",
4: "Bottomless Pot: After twenty minutes over a fire, magically provides enough to feed fifty",
5: "Utility Apron: Extra-dimensional pockets in easy reach, and keeps clothing clean beneath",
6: "Spoon of the Beefeater: Detects poison in any food or drink it touches",
7: "Plaid Thermos: Provides an endless supply of hot soup that helps to cure most diseases",
8: "Mitts of the Hearth Keeper: Provides wearer resistance to fire damage",
9: "Knife of Paring: A magically sharp knife that can reduce a targets armor by one on a hit",
10: "Cap of the Connoisseur: Tall pleated hat increases sense of taste, smell, and intelligence ",}
cook_antagonists = {1: "Silver Spoons: Believe only the upper class can truly appreciate flavorful food and drink",
2: "The Combine: Buys direct from farmers to monopolize and gouge food prices in town",
3: "Iron Chefs: Resort to underhanded tactics to undermine any perceived competition",
4: "Pious Palate: View colors, flavorful foods, and much else as distractions from holiness",
5: "The Secret Ingredient: Secretive assassins that use poison to ensure a victim's last meal",
6: "Purists: Preach their super restrictive diet as the best for all, to the annoyance of many",}
cook_rivals = {1: "The Devil's Larder: Where a man-eating monster stores its victims before consumption",
2: "Giant's Cauldron: Volcanic cooking area where huge scale meals are prepared",
3: "Enchanted Gardens: Fey-touched fruits that are irresistible, delectable, and dangerous",
4: "Wizards Kitchen: Elementally fueled appliances and a host of strange ingredients",
5: "The Ice Box: Frozen fortress where an evil army is laying away stores, attracting monsters",
6: "Confectionery Cottage: A hag's hut made of candy to attract the curious and hungry",}
cook_locs = {1: "Tacito Watende: Wandering cook who gains reputation mostly by tearing others down",
2: "Dentaun Ego: Harsh critic who is never satisfied and wants everyone to know it",
3: "Killian Wellogg: Noble who advocates for bland foods to keep the commoners docile",
4: "Chipo the Butcher: Uses his meat shop as a front for his ring of petty criminals",
5: "Yeba Zub: Glutton whose manners make anyone nearby quickly lose their appetite",
6: "“Whiskers” Blasula: Their “pets” often find their way into pantries and kitchens uninvited",}
cook_monsters = {1: "Pepperbush Blight: Explosively spicy plant monster that causes fire and acid damage",
2: "Enchanted Dough: Slow moving but always growing larger, engulfs anything in its way",
3: "Animated Cutlery: Plates, silverware, and kitchen knives that attack the unwary",
4: "The Hunger: Insatiable undead with a cavernous stomach and a tiny mouth",
5: "Grease Trap Gremlin: Mischievous creatures that enjoy ruining dishes, and starting fires",
6: "Brain Eater: Eldritch abominations who consider the minds of the sentient a delicacy ",}
cook_plot_hooks = {1: "The hunt for a mythical beast has been called so it may be served at the king's coronation feast",
2: "Someone tried to gain an edge at the festival's cook-off and unleashed magical havoc",
3: "A ceremonial meal prepared as sacrifice for a god was inadequate, and now the god is angry",
4: "A wizard's spellbook was swapped for a cookbook, and there was dangerous magic in there",
5: "Trouble on the road has made several ingredients hard to come by in town",
6: "A feast is prepared fortnightly and delivered to the dragon, but people are beginning to go hungry",
7: "A strange illness sweeps through the city, unsanitary kitchens are blamed, but the truth is worse",
8: "The tyrant hosts huge banquets as a show of power, and sometimes reveals his next moves there",
9: "An underwater threat has devoured all the seafood, and likely several fisherfolk as well",
10: "A band of ravagers is killing livestock and setting fields aflame, threatening the town with famine",
11: "The warring sides must come to the table to break bread, but first we might have to break heads",
12: "The line between food and medicine is blurry, and a rare ingredient may save the day",
13: "The symphony of aromas rising from the wedding buffet has attracted uninvited guests",
14: "A long lost recipe is rumored to lie somewhere in the nearby dungeon",
15: "The taste of ash permeating all the food and drink was the first sign of impending doom",
16: "The monstrous brute's consumed almost every morsel, it's feared it will start eating people next",
17: "A local dish encodes mythical knowledge of a nearby treasure, and its guardian",
18: "A cult is committing atrocities in the name of its deity's strange appetites",
19: "The tavern's cook didn't always work in kitchens, and their past has caught up to the them",
20: "It will be impossible to get a good meal around here until peace is restored",}

criminal_drives = {1: "Clear a debt that's been hanging over them",
2: "Free a loved one held by a rival gang",
3: "Avenge themselves on their old organization",
4: "Earn the right to build a better, safer life",
5: "Rise to the very top of the crime world",
6: "Become a legend of story and song",
7: "Take back something that was stolen",
8: "Prove to everyone that they've been reformed",
9: "Make up for past wrongdoings",
10: "Return honor to the world of thieves",
11: "Amass ill-gotten gains and retire in luxury",
12: "Free family from squalor and poverty",
13: "Earn the respect of “legitimate” society",
14: "There is no high like the thrill of the heist",
15: "Rise above their humble, harsh beginnings",
16: "Make their way in a world that's never easy",
17: "Outrun the authorities and keep past secret",
18: "Provide for their under-served community",
19: "Pull off the greatest job of all time",
20: "Heroically sacrifice everything for their crew",}
criminal_catalysts = {1: "Raised to honor the criminal code",
2: "“The Law” destroyed their family as a child",
3: "Adopted by a legendary criminal in youth",
4: "Wrongfully imprisoned, branded a criminal",
5: "Stumbled into aftermath of heist gone wrong",
6: "The city guard are just another criminal gang",
7: "Blackmailed into thievery, discovered knack",
8: "Aged out of orphanage with no other skills",
9: "Married into crime family and wanted to fit in",
10: "Stories from a cellmate while serving time",
11: "Highly romanticized view of a life of crime",
12: "The criminal underbelly is their only family",}
criminal_growth = {1: "Petty pickpocket, to criminal mastermind",
2: "Reckless thrill seeker, to strategic thinker",
3: "Wanted felon, to celebrated hero",
4: "Paranoia of others, to trust and family",
5: "Save yourself mentality, to saving the world",
6: "The path of redemption and transformation",
7: "Penniless outcast, to landed gentry",
8: "The hardened criminal slowly going soft",}
criminal_friends = {1: "Midnight's Ravens: Clandestine couriers and messenger service operating in code and cant",
2: "The Crickets: Street kid beggars and pickpockets with eyes and ears all over city",
3: "Ghost Shippers: Smuggler network that can get nearly anything, in time, for the right price",
4: "Teamsters Guild: Lifeblood of commerce, who will occasionally let goods “fall off the wagon”",}
criminal_assets = {1: "“Quiet” Jaffrey: Second story man who never shuts up, especially if he's been drinking",
2: "The Lady Bluebird: Mysterious aristocratic backer who's paid for several strange jobs in the past",
3: "Elena Rider: Sells flowers and has an exquisite hand for forgeries",
4: "Tam MacKay: Tinker who doubles as a fence and can identify magic items",
5: "Arlen Leaby: Lazy but mostly honest member of the city watch, who was a childhood friend",
6: "“Grey” Mable: Grandmotherly proprietor of a quaint B&B, paid for by a life of crime",}
criminal_items = {1: "The first copper they ever picked from someone's pocket successfully",
2: "A broken set of lock picks that once belonged to a mentor",
3: "Whispering Stones: Paired stones that allow communication between them twice per day",
4: "Glitter Bomb: Creates a loud and colorful explosion, does no damage but very distracting",
5: "Silent Satchel: Opens into a small extradimensional space which traps sound",
6: "Boots of the Nightcrawler: Aid wearer in climbing and moving with stealth",
7: "Fine Thieves Tools: Grants benefit on all checks to pick locks and disarm traps",
8: "Blade of Shadow: +1 dagger that can magically collapse into the gem on the pommel",
9: "Cloak of the Chameleon: Can shift tone and texture to match surroundings and aid in hiding",
10: "Gloves of Pilfering: Grant an advantage when thieving or using sleight of hand",}
criminal_antagonists = {1: "Cutpurse Alliance: Seek to unify all criminals under their umbrella, and collect their percentage",
2: "Golden Giants: Elite Gentlemen's club of aristocrats who break the law and bribe officials",
3: "Divine Reprisal: Hard line religious zealots who mete out punishment as they see fit",
4: "Steel Shepherds: Caravan guards who wear thieves' hands they've cut off as trophies",
5: "Bloodhound Brotherhood: Bounty Hunters, very comfortable with collateral damage",
6: "Silvered Eye: Scry network surveying the populace's homes and minds to prevent crime",}
criminal_rivals = {1: "Quayside: Seedy neighborhood of docks, warehouses, and bars around smugglers' piers",
2: "The Opalescent Vault: Famous bank with magically protected safety deposit boxes",
3: "Hell's Gate: Prison Complex that is supposedly impossible to escape from",
4: "Rock Dove Gantries: Secret network of rooftop paths, planks, and hideouts above city",
5: "Flee Bottom Market: Collection of vendors in slums where almost anything can be bought",
6: "The Pit: Ancient, abandoned prison overrun by monstrous descendants of trapped inmates",}
criminal_locs = {1: "Devone Little: Strong arm robber with a personal code to only target criminals",
2: "“Eagle Eye” Iorana: Watch captain with a personal grudge just waiting for them to slip up",
3: "“Spider” Rhys: Spymaster who uses info to build their web of leverage and blackmail",
4: "“King” Corman: Narcissistic gang boss who is jealous of more powerful criminals",
5: "Germaine “The Hammer” Huwart: Gladiator turned enforcer, it pays better with fewer rules",
6: "“Whisper” Victi: Changes identity each time they deceive and double cross their compatriots",}
criminal_monsters = {1: "Rat Pack: Bandits cursed with lycanthropy who swarm in sewers and dungeon entrances",
2: "Gargoyle: Animate flying statues, typically found on roofline guarding buildings",
3: "Brownies: Tiny industrious fey who complete household tasks and steal if uncompensated",
4: "Disguised Devil: Runs crime ring as means to efficiently obtain souls",
5: "Loot Drakes: Flying serpents who covet wealth, poisonous and tamable",
6: "Vengeful Angel: Radiant, has unnuanced views of morality and a big flaming sword",}
criminal_plot_hooks = {1: "The McGuffin must be stolen and replaced with a replica before the cult can complete their heist",
2: "A turf war between rival gangs is spilling over as the sides recruit monsters and mages to fight for them",
3: "A new drug with magical side effects is flowing in, threatening to devastate whole communities",
4: "Underworld leaders are being assassinated and the resulting power vacuum leads to chaos",
5: "The race to take the ancient artifact from the trapped tomb is on, now that a map was discovered",
6: "An old partner in crime resurfaces with a plan for one last lucrative score",
7: "They may be guilty of other crimes but they've been framed for this one and must clear their name",
8: "A mentor figure returns, forced out of retirement and in desperate need of help",
9: "A secretive noble is recruiting powerful figures from the edges of society for a dangerous mission",
10: "The old gang's under new leadership and things have taken a much darker turn",
11: "A legendary criminal is said to have made their hideout, and hid their treasure, inside the dungeon",
12: "A squad of expendables has been gathered, facing certain death for their freedom",
13: "The wizard pays very well, but what are they building with all of these stolen relics?",
14: "The monstrous marauders follow whoever killed their last leader, but are difficult to control",
15: "A notorious criminal must be captured alive, and escorted to a high security prison",
16: "The monster claims it was just a patsy following orders from a sinister figure in the shadows",
17: "Bandits have learned to target adventurers leaving the dungeon, because they are damaged and treasure-laden",
18: "The leader's loved one was has been kidnapped, and they seek help beyond the law to get them back",
19: "A desperate, fleeing thief hands off a package to the party, starting a series of falling dominoes",
20: "Coded messages in thieves' cant reveal the possible source of the monsters' location",}

cultist_drives = {1: "Evangelize the faith and grow its numbers",
2: "Achieve eternal reward through sacrifice",
3: "Gain renown to glorify their god",
4: "Prepare for the prophesied end",
5: "Protect others in their chosen family",
6: "To rise in power and take a leadership role",
7: "Uncover the forbidden sacred knowledge",
8: "Continue the cult's traditions and rituals",
9: "Gain societal acceptance and respect",
10: "Become an avatar or deity in their own right",
11: "Establish a utopian community",
12: "Convert influential and powerful figures",
13: "Cleanse the world of the unworthy",
14: "Reveal the truth to an unsuspecting world",
15: "Pave the way for deity's arrival or return",
16: "Secretly spread the group's reach",
17: "Gain strength to confront ridicule",
18: "Usher in the promised golden age",
19: "Enact the inscrutable will of their god",
20: "Interpret the signs that are all around us",}
cultist_catalysts = {1: "Uncovered an ancient sacred text",
2: "Visions and whispers from a forgotten god",
3: "Outside persecution for their beliefs",
4: "Desperate need for meaning after tragedy",
5: "The central prophet has died mysteriously",
6: "A schism in the group they must heal",
7: "The deity suddenly stopped communicating",
8: "A celestial event is interpreted as a portent",
9: "False doctrine spreads and must be stopped",
10: "Membership is dwindling to nothing",
11: "Inherited the faith and a sacred obligation",
12: "Mentored by a charismatic leader when lost",}
cultist_growth = {1: "From true believer, to free thinker",
2: "Fringe figure, to mainstream acceptance",
3: "Doubt and disillusion, to new form of faith",
4: "Lowly seeker, to sainthood, to apotheosis",
5: "Mindless follower, to thoughtful leader",
6: "Thwarting an end time they once sought",
7: "Misguided and misled, to self-actualized",
8: "Establishing a healthier version of faith",}
cultist_friends = {1: "The Veil Piercers: Faux secret club of wealthy collectors of the occult and esoteric",
2: "Shadow Singers: Wandering bards who seed the faith in the guise of stories and songs",
3: "Twilight Gardens: Herbalists who concoct potions, including those used in cult's rites",
4: "Obsidian Archive: Believe in preserving all knowledge, even if potentially dangerous",}
cultist_assets = {1: "Balmyr Drul: Disguised fey creature who is obligated to help cult members for next decade",
2: "Kalas Voltar: Scarred hermit marked by direct experience with the cult's deity",
3: "Garvin Black: Smith who doesn't believe but asks no questions about ceremonial daggers",
4: "Brev Fiori: Ostracized member who became a gravedigger, prefers the company of the dead",
5: "Mervo the Marvelous: Charlatan fortune teller who takes nothing seriously",
6: "Plunk: Wide-eyed neophyte who just joined and idealizes existing members",}
cultist_items = {1: "A lock of hair: A last memento from the time before they joined the cult",
2: "Aromatic Censer: Produces thick, scented smoke that can obscure a small area",
3: "Ritual Dagger: Does an extra die of damage while wet blood is on its curving blade",
4: "Darkstone: Each midnight can answer one knowable yes or no question about the next day",
5: "Hallowed Grimoire: Adds a +1 to all spells cast within the deity's domain, school, or type",
6: "Robe of the Dark Flame: Wearing this robe instills resistance to holy radiant damage",
7: "Brand of Belonging: Mark of initiation that instills or improves the ability to see in darkness",
8: "Brass Astrolabe: Complex astronomical model that predicts large upcoming events",
9: "Eclipse Gem: Creates an area of magical darkness for one minute once per day",
10: "Soul Ring: Can hold one soul at a time of recently defeated creature for 5 questions",}
cultist_antagonists = {1: "New Dawn's Radiance: Worshipers of a vengeful sun god trying to eliminate other faiths",
2: "The Rising Tide: Merchants Guild who think old “superstitions” stand in the way of their trade",
3: "Culture Coven: Scholars trying to make all knowledge public, including cult secrets",
4: "Inquisitive Eye: Zealous promoters of their own, strict interpretation of their deity's will",
5: "Crimson Crusade: Follow a different god and are trying to fulfill it's prophecy of destruction",
6: "Orthodox Key: Believe one unified faith will bring peace and go to any length to make it so",}
cultist_rivals = {1: "Dark Cathedral: Secret and windowless house of worship, dim light or none at all",
2: "Obsidian Monolith: Amplifies magical effects but of mysterious, unknown origins",
3: "Sunken Temple: Buried site of worship for a long forgotten god, recently repurposed",
4: "Shattered Isle: Mythical location of lost city that disaster befell",
5: "Barrow Hill: Desecrated burial site teeming with relics and ancient undead",
6: "The Darchive: Hidden library containing forbidden texts and rolling ladders",}
cultist_locs = {1: "Prelate Naasir: Sees cults as an insult to the faith that they follow",
2: "Matron Peitra: Motherly figure of a rival cult with dark undertones beneath sweet promises",
3: "Parson Yugo: Haplessly confused a ritual and is now secretly possessed by a demon",
4: "Kelvanus Kean: Uses charisma and enchantement to gain followers, and their silver",
5: "Curate Aulus: Corrupt clergy who sells useless cures and blessings",
6: "Scarla Thorne: Exiled cult member seeking revenge on those who ostracized her",}
cultist_monsters = {1: "Shadow Beast: Dark creatures summoned to serve for one day, then feral and free",
2: "AntiPaladin: Champion of an evil god who wields necrotic powers to smite enemies",
3: "Radiant Guardian: Celestial creature still protecting an abandoned ancient holy site",
4: "Arachno Demon: Eight-armed monstrosity from the darkest depths of the abyss",
5: "Wights: Reanimated cult members undead after failed ritual for immortality",
6: "Void Naga: Serpentine relic from lost age who once followed the same deity",}
cultist_plot_hooks = {1: "Track down the artifact to complete the ritual, but don't let the others know why it is needed",
2: "Rumors are a rival cult has gained subtle influence over the town, the locals are acting funny",
3: "An unlikely NPC becomes an eager new convert, and believes they've received a message",
4: "An obscure text reveals the cult's origins are not what they seem, and that they're being used",
5: "Dreams and visions featuring the cult's patron begin disturbing everyone's rest",
6: "The cult is being scapegoated, or perhaps it was their fault after all",
7: "Misguided members must be stopped before they perforn the ceremony to open the seals",
8: "The cult must be infiltrated to extract brainwashed members who are there against their will",
9: "The deeper truth the cult is seeking, or is avoiding, can only be found on another plane",
10: "The founder's reliquary has been stolen and must be recovered before it is used nefariously",
11: "A prophesied comet is seen that portends a climactic event, unless the party intervenes",
12: "Leadership requires a task be performed before initiation into the cult's highest truths",
13: "The cult's worship is actually pacifying an evil deity, undermining their practices may awaken it",
14: "Something is causing deities to fall silent, the cult's patron could be next, or the cause",
15: "The party must uncover an ancient holy site for a chance to recover a long lost reagent",
16: "Flashy acts of heroism could be the fastest way to increase reputation, where the monsters at?",
17: "A cult member has gone mad and is trying to recruit a dragon better left alone",
18: "Statues depicting deities have begun animating, and running amok",
19: "An obscure ritual is the key to opening the passage into the underground labyrinth",
20: "Innocents are being sacrificed to a rival god, along with everybody else",}

detective_drives = {1: "Prove they are the best in the world",
2: "Crack the cold case that changed their life",
3: "Outsmart and thwart crime in all its forms",
4: "Free the simple folk from evil and corruption",
5: "Redeem themselves after a botched case",
6: "Return their stolen family fortune",
7: "Untangle the web of the infiltrating cult",
8: "Retire in leisure and write their memoir",
9: "Best their nemesis, who's one step ahead",
10: "Solve the unsolvable mysteries of life",
11: "Protect civilization from lawlessness",
12: "Uphold divine principles of truth and justice",
13: "Capture criminal kingpins as an example",
14: "Serve as a symbol for the next generation",
15: "Rehabilitate their fallen town or district",
16: "Gain historical or literary renown",
17: "Do their best within the system of law",
18: "Provide justice beyond the letter of the law",
19: "Overcome savagery with sophistication",
20: "Finally understand how it all fits together",}
detective_catalysts = {1: "Mysterious disappearances during their childhood",
2: "Family impacted by a wave of crime",
3: "Witness to an incredibly daring heist",
4: "Leader found dead, leaving many questions",
5: "Abuse of power from law enforcement",
6: "A parent figure was framed or scapegoated",
7: "Early fascination with puzzles and ciphers",
8: "A kindly constable mentored them",
9: "Sheer boredom of aristocratic lifestyle",
10: "Repentant criminal given a second chance",
11: "Greatly deceived once, but never again",
12: "Making up for the lack of another talent set",}
detective_growth = {1: "Skeptical cynic, to having their faith restored",
2: "Haughty hubris, to trusting in others",
3: "Dispassionate observer, to empathic member",
4: "Hard-nosed “realist,” to optimistic idealist",
5: "Obsessed with past, to focused on the future",
6: "Gruff loner, to passionate teammate",
7: "Needing to know, to embracing the mystery",
8: "Making peace with the idea they can't solve it all",}
detective_friends = {1: "A friendly murder of crows: Way smarter than most people think, gift clues and keep look-out",
2: "Lamp Lighters: Oft-ignored workers who maintain the streets and quietly observe much",
3: "Silvered Scales: Guards and barristers trying to confront corruption inside the legal system",
4: "Veil Watchers: Mendicant sect worshiping the god of knowledge who seek wisdom over all",}
detective_assets = {1: "Illian Black: True neutral pawnbroker and parttime fence with friends in very low places",
2: "Melanie Manyface: Joyfully infiltrates any level of society, for a substantial price of course",
3: "“Glum” Marvin: Morose ghost of back-stabbed murder victim, drops cryptic clues on occasion",
4: "Maria Morstan: Runs a tavern and is always in the know about local rumor mill",
5: "Major Halpern: Curmudgeonly retired city watch leader filled with stories and advice",
6: "Zvi Covenya: Tinker who crafts useful tools and has several areas of extensive knowledge",}
detective_items = {1: "A beat up old badge they keep hidden, could be a souvenir, a keepsake, or a trophy",
2: "Sheaf of notes on an unsolved mystery, wrinkled, dogeared, and annotated",
3: "An exquisitely crafted magnifying glass that aids in investigation checks",
4: "Mind Palace: A magical tome that aids in recalling knowledge but requires a short rest",
5: "Hartstalker Hat: Shades the face and neck, grants an advantage when checking for tracks",
6: "Lens of Deciphering: Translates any written language viewed through it, one page per day",
7: "Cape of Disguise: Uses illusory magic to alter appearance at will and protects identity",
8: "Clue Compass: Points in the direction of a named object if within a quarter mile",
9: "Shadow Soled Boots: Not only improve stealth but they're also quite fashionable",
10: "Pearl of Identification: Once per day can identify magic items and their properties",}
detective_antagonists = {1: "Ebon Rose: Assassins for hire, excel at making it look like an accident",
2: "The Gritty Syndicate: Petty criminals who don't quite cross the line to true evil",
3: "Blood Pact: Lawless mercenary force, dangerous on the battlefield and also at the bar.",
4: "Iron Octagon: Underground fighting ring, distrusts outsiders but still takes their bets",
5: "Chainbreakers: Cult of imprisoned evil god, practice freeing prisoners as act of worship",
6: "The Sophisticated Scoundrels: Elites who unfairly wield their influence to grow richer still",}
detective_rivals = {1: "The elegant mansion turned scene of the crime, perhaps during a dinner party",
2: "The maze of narrow alleys where the darkest parts of the city get swept",
3: "Serene Shore: Desolate but beautiful stretch of coast where disappearances happen often",
4: "Dark Market: Black market vendors that set up in a different secret location each night",
5: "Clock Tower: Filled with moving mechanisms, grand views, and steep falls",
6: "The Moors: Barren highlands of acidic peat and boggy patches to sink into",}
detective_locs = {1: "The Professor: Mysterious criminal mastermind credited for many audacious heists",
2: "Shuma Zabul: Stuttering apothecary rumored to be an expert in concocting poisons",
3: "Severin the Serpent: Charismatic gang leader whose underlings do all the dirty work",
4: "Lady Inanna: Charlatan who enjoys the game of parting the unsuspecting of their coin",
5: "Adomi Thwaite: City watchman easily bribed to look the other way, often already was anyway",
6: "Mauro Gaspare: Rival detective whose selfpromotion outshines his powers of deduction",}
detective_monsters = {1: "Gallows Ghosts: Spirits of hung criminals returned to sow chaos",
2: "Enigma Sprites: Tiny, mischievous fey who enjoy puzzles and puns",
3: "Shadow Stalker: Incorporeal dark spirit magically summoned with a target to kill",
4: "Fear Mongers: Monsters that instill fear in their victims, clouding their judgment",
5: "Sphinx: Powerful guardians of important sites who famously deal in riddles",
6: "Revenant: Restless undead seeking revenge for their wrongful death",}
detective_plot_hooks = {1: "A crime wave on the roads hinders trade, but the bandit hideout proves difficult to find",
2: "A string of victims where cryptic notes are left behind by the killer",
3: "Urchins are disappearing from the streets but few seem to care",
4: "A seance at an elegant dinner party inadvertently unleashes a great evil",
5: "Goblins are blamed for recent troubles around town, but the truth is not so simple",
6: "A heist must be performed to prove an artifact is a replica and has already been stolen",
7: "Ancient statues scattered around the city are actually clues pointing to the location of a treasure",
8: "A noble is paying a bounty to attempt to break into their manor to test their new security",
9: "Framed for a crime they didn't commit, they will have to find the perpetrator to clear their name",
10: "The person paying a huge bounty to steal an item is secretly the item's owner, because it's cursed",
11: "A cult is threatening the regions safety, but membership is secretive, anyone could be part of it",
12: "The line between the city watch and the criminal gangs has become very blurry",
13: "Uncovering hidden truths from the past may be the key to preserving any hope for the future",
14: "Discovering the truth of the prince's lineage could be the only way to avert disaster",
15: "Someone, or something, is wreaking havoc by impersonating authority figures around town",
16: "It appears the bride-to-be was kidnapped, but maybe was she escaping an arranged marriage",
17: "The guardian can't be overcome physically but will yield if defeated in a battle of wits",
18: "Someone is opening portals to other planes, releasing dangers into this world in the process",
19: "The crime lord has been arrested, unleashing a destructive power struggle in the underworld",
20: "Rumors of a humanoid beast suggests there is a lycanthrope in their midst",}

emmissary_drives = {1: "Establish lasting peace between nations",
2: "Promote their own culture and people",
3: "Deliver a message to a far off leader",
4: "Open new routes and markets for trade",
5: "Lift up the marginalized in foreign lands",
6: "Foster exchange between cultures",
7: "Redeem the reputation of their homeland",
8: "Spread awareness of a growing problem",
9: "Forge alliances to help liberate their home",
10: "Gain esteem and historical recognition",
11: "Contact new and unusual cultures",
12: "Convince others to visit their country",
13: "To serve as a bridge, creating unification",
14: "Acquire wisdom from diverse lands",
15: "Create respect between civilized peoples",
16: "Speak softly and carry a big stick",
17: "Promote tourism to their region",
18: "Serve as a shining example of their people",
19: "Implement a united league of good nations",
20: "Synthesize the best from all cultures",}
emmissary_catalysts = {1: "Steeped in social diplomacy since birth",
2: "Decorated solider now promoting peace",
3: "From an overlooked, unknown population",
4: "They were appointed by authority figures",
5: "Royalty bored by life of luxury",
6: "Want to put all of their knowledge to use",
7: "They just could not stay in their homeland",
8: "Devastated by past wars, never again",
9: "Desire to see all the places they've studied",
10: "Seeking power after subjugation",
11: "Romantic dalliance with a betrothed royal",
12: "Witnessed that pen is mightier than sword",}
emmissary_growth = {1: "Outdated book smarts, to earned experiences",
2: "Aloof and reserved, to fully going native",
3: "Distrusted outsider, to member of community",
4: "Adapting to and overcoming cultural barriers",
5: "Naive envoy, to shrewd negotiator",
6: "Rigid absolutist, to moral relativist",
7: "Shaky in a second language, to fully fluent",
8: "Tentative observer, to confident influencer",}
emmissary_friends = {1: "Expat Community: Small but tight-knit pocket of other people from their homeland",
2: "The Stacks: High-ceilinged library where librarians speak and translate many languages",
3: "Embassy Club: A booth in a local tavern where other dignitaries meet and mingle",
4: "Unblinking Eyes: Embedded spies and informants that harvest information of all kinds",}
emmissary_assets = {1: "Dame Adelia Hail: Aristocrat who can help navigate high society, in exchange for stories",
2: "Franklin Benjamin: A witty envoy from another nation who also tinkers with artifice",
3: "Evran Wavefarer: Retired sailor who traveled to many foreign lands, and learned their curses",
4: "Robyn “The Bird” Snuggs: Runs the staff of government buildings, and a lucrative rumor mill",
5: "Osaze Sogdu: Another stranger in a strange land, “O” to friends and secretly a sorcerer",
6: "Zephyr Swiftly: Messenger whose near-ceaseless talk is a fast as their deliveries",}
emmissary_items = {1: "An official seal that serves as proof that they speak for the leadership of their homeland",
2: "An honorary metal from a foreign military that garners great respect in some circles",
3: "Ink-filled quill: Ingenious invention, allows for writing on many surfaces without an inkwell",
4: "No Hassles Cloak: Magically transforms appearance to match local clothing styles",
5: "Tome of Translation: Given an hour of study this can translate nearly any written language",
6: "Insightful Cravat: Gently tightens on wearers neck when that person is being lied to",
7: "Silver Tongue Elixir: Grants ability to speak in any language, though not to understand it",
8: "Binding Treaty: Any who sign this agreement suffer psychic damage if they break their word",
9: "Boots of the Traveler: Increases movement speed by half again unless encumbered",
10: "Circlet of the Unifier: Grants an advantage on all persuasion and diplomacy checks",}
emmissary_antagonists = {1: "Ironwood Table: A group of nobles who jealously guard their influence and identities",
2: "The War Hawks: Cabal of business owners who profit off of the conflicts they seed",
3: "The Quiet Ears: Vast spy network that infiltrates serving staff and trades in secrets",
4: "The Emerald Delegation: Diplomats from another realm who are haughty and dismissive",
5: "Golden Blossom: Cult-adjacent separatist group set against the current order",
6: "Detached Contingent: Isolationists who want to see their land free from “foreign influences”",}
emmissary_rivals = {1: "Chamber of Conversation: Ornate structure suffused in abjuration wards and anti-magic",
2: "Shattered Monument: Memorializes an ancient treaty, toppled in later wars",
3: "The Enclave: Abandoned settlement of expats, new occupants mock culture's traditions",
4: "Court of Ghouls: Home to haughty undead, rather eat the living than negotiate with them",
5: "Bald Crag: Exposed cliff where monstrous bands meet to form often uneasy alliances",
6: "Dread Halls: Puzzles and traps enforce the original builder's twisted sense of decorum",}
emmissary_locs = {1: "General Stonehammer: Distrusts diplomacy and only values military solutions to issues",
2: "Cypher: Pseudonym of a mysterious figure undermining peace efforts from the shadows",
3: "Baron Grax: Xenophobic noble who believes in a hierarchy of peoples, with his kind on top",
4: "The Brokerage: Crime chief who has learned state secrets are the most valuable commodity",
5: "Ixar: Proclaims foreigners carry demonic influence, was right once and gained a following",
6: "Captain Blacktooth: Supposedly retired pirate, an anarchist who hates organized states",}
emmissary_monsters = {1: "Stone Guardian: Inscrutable and untouchable, combat not a viable option to get beyond it",
2: "Banshee: Vengeful spirit of a murdered messenger from another culture",
3: "Incubus/Succubus: Devil who seems willing to change evil ways, but it's a ruse to get close",
4: "Pactkeepers: Powerful celestials that can be summoned to witness, and enforce, oaths",
5: "Psionic Siren: Aberrant envoy claiming to seek allies, really seeking slaves and subjects",
6: "The Winged King: Dragon with crown-like horns, demands tribute from all in their domain",}
emmissary_plot_hooks = {1: "A war between evil tribes is spilling over into more civilized lands and harming innocent bystanders",
2: "The caravan carrying the region's tribute to the evil overlord was attacked and robbed",
3: "An ambassador from a foreign power disappeared mysteriously, threatening a fragile peace",
4: "War mongers seeks to disrupt the royal wedding that is set to unify the empire",
5: "A long lost relic of their people is rumored to be located deep within dangerous territory",
6: "Long used trade routes have grown progressively more unsafe, undermining several economies",
7: "Historical adversaries must agree to work together if they hope to survive a much bigger threat",
8: "Postponing a ritual observance accidentally breaks a long-forgotten agreement with a mythic force",
9: "Someone has been impersonating officials to sew chaos, and they're growing more brazen",
10: "A federation of undersea ancestries seeks aid from the coastal cities against an aboleth's hoard",
11: "Beings from other planes host a summit nearby, but see the inhabitants of this world as nuisances",
12: "Parlaying with or infiltrating a notorious smugglers' ring may be the only way behind enemy lines",
13: "The heir apparent fancied themselves an adventurer, and has gone missing in a dungeon",
14: "A foreign dignitary requires safe passage home, after their ship was lost to a monster attack",
15: "The hoard is evil but lawful, and understanding their complex honor system could be instrumental",
16: "A natural disaster exposes a valuable resource, and a mad rush among the factions to claim it",
17: "A heraldic beast has been spotted for the first time in centuries, it's fate has prophetic implications",
18: "Extracting an asset from a city under siege is the only way to advance the hunt for the McGuffin",
19: "Mad or misguided, leadership is engineering an apocalypse, but working against them is treason",
20: "A fallen citadel must be reclaimed to preserve an ancient alliance and time is running out",}

entertainer_drives = {1: "Single-handedly revive a dying art form",
2: "Spread joy in a world filled with hardship",
3: "Leverage their abilities to escape the past",
4: "Be recognized as the greatest of all time",
5: "Seek out inspiration to elevate their act",
6: "Bring a smile to a special someone's face",
7: "Outshine another specific performer",
8: "Preserve and protect passed-down tradition",
9: "Show the transformative power of story",
10: "Gain the attention of as many as possible",
11: "Uncover and disseminate ancient works",
12: "All the world's a stage, might as well play",
13: "Become an inspiration to future generations",
14: "Connect to as many people as possible",
15: "Amass wealth and build a great theater",
16: "An insatiable need for praise and approval",
17: "Laughter is a healing light in the darkness",
18: "Act on the knowledge hidden in folklore",
19: "Nothing is as satisfying as fame",
20: "Prove their worth and leave a mark",}
entertainer_catalysts = {1: "Trained by a harsh but brilliant mentor",
2: "A performance shaped them as a child",
3: "Performing helped them find their voice",
4: "Songs and tall tales may contain the truth",
5: "Much can be observed entertaining at court",
6: "A traveling troupe expands their worldview",
7: "An enamored audience will tell you a lot",
8: "Oppressive political forces stifle expression",
9: "Peace is required for entertainment to thrive",
10: "Enemy arrows, rotten tomatoes, same thing",
11: "Secrets found while seeking new material",
12: "The muses can inspire and make demands",}
entertainer_growth = {1: "Transmitter of history, to generator of history",
2: "Entertaining for survival, then to thrive",
3: "Performing on corners, to the largest stages",
4: "False persona, to self acceptance",
5: "Feeding the ego, to focused on audience",
6: "Big fish in small pond, tossed into the deep",
7: "Arrogance, to humility, to poise and grace",
8: "From a struggling unknown, to beloved star",}
entertainer_friends = {1: "Strife & Draum: Marching band of retired veterans who spread peace through music",
2: "Merry Pranksters: Traveling troupe who puts on psychedelic shows fueled by illusion magic",
3: "Golden Chorus: Singers whose harmonies have healing properties",
4: "The Hushed Circus: Perform balletic, acrobatic stunts in perfect silence, hear much",}
entertainer_assets = {1: "Eurus the Wind Dancer: Their hypnotic performances can influence the weather",
2: "Thimblerig Jale: Fast-talking magician who often makes their audience's coins disappear",
3: "Yuke Hamlin: Musician with the ability to attract or drive off small beasts with music",
4: "Booker T. Scallion: Connects taverns and inns to entertainers, aspires to grander venues",
5: "Muriel Starreader: Fortune teller who rarely uses divination, but rather give good news",
6: "Old Livy: Traveler who tells the news and history for a living, collects stories and spoons",}
entertainer_items = {1: "Broken Quill: A significant work, to the world or just to them, came from it's worn down nib",
2: "The autograph of a famous performer, valuable for fans, collectors, and forgers alike",
3: "Feathered Flutes: Imitate bird calls as covert signals, occasionally attracts a real bird",
4: "Muslin Veil: Alters the wearer's facial appearance twice per day",
5: "Choker of Amplification: When activated can carry voice clearly 300' through air",
6: "Cloak of Many Colors: Spinning rapidly while activating this creates a mesmerizing display",
7: "Pipe of the Tale Teller: Smokey illusions illustrate the user's story while lit",
8: "String-less Marionette: Can animate once daily, following commands for 10 minutes",
9: "Somnolent Strings: Harp that induces a magical drowsiness to overtake targets",
10: "Charismatic Crown: Increases wearer's charisma while attuned",}
entertainer_antagonists = {1: "The Solemn Vow: Music and dancing are an affront to the beliefs of this religious order",
2: "Strength Weavers: Require all entertainment to celebrate and support the current hierarchy",
3: "The Rabble Rousers: Inflame hatred and violence under the guise of irreverent comedy",
4: "The Thieves of Joy: lawless bandits who masquerade as traveling performers",
5: "The Silver Circle: Wealthy critics who disparage any art form they see as lowbrow",
6: "Jests & Jugglers: Local act who wants to partner with others, but they are simply awful",}
entertainer_rivals = {1: "Fey Stage: Fairy circle on sloping hill side where illusory magic is twice as potent",
2: "Dread Ballroom: Haunted hall where the ghostly inhabitants covet new dance partners",
3: "Silent Halls: Ruins of a monastery where a magical silence persists",
4: "Floating Forum: Venue where the stage and several layers of seating are floating in air",
5: "King's Theater: Festooned with false sets, trapdoors, curtains, and catwalks",
6: "Ancient Amphitheater: Tiered seating creates potential cover and height advantages",}
entertainer_locs = {1: "Thadius Darkstring: Entertainer who sabotages others to improve his own standing",
2: "“Busker” Sym: Plays improvised drums on corner for coppers, inexplicably hates heroes",
3: "The Reactionary Rake: Whole act is based on responding negatively to the work of others",
4: "Goody Dinah: Obsequious tavern owner who is a terror to all who work for her",
5: "“Heckler” Vic: Failed acolyte who drunkenly interrupts performances with slurred sermons",
6: "Jeero: Silent clown who seems to derive great joy from sneaking up and startling others",}
entertainer_monsters = {1: "Vocal Fries: Small fey who steal victim's voice and use it in mocking songs",
2: "Farce Demons: Imps that set slapstick traps and evoke hideous laughter",
3: "The Fat Lady: An operatic spirit who combines the powers of banshee and siren",
4: "Shadow Puppets: Arise from a magic lantern suffused with necrotic energy",
5: "Gloom King: Legions of his minions capture victims to force them to perform for him",
6: "Dread Dancers: Eerie music draws victims, mesmerizing moves paralyzes witnesses",}
entertainer_plot_hooks = {1: "An annual performance keeps dark forces at bay, though few remember the significance",
2: "A curse has rendered nearly every performance in a certain theater a tragedy",
3: "Valuable objects, and now even people, seem to go missing when a certain troupe comes to town",
4: "A melody seems to drive those who hear it temporarily mad, until they transmit it to someone else",
5: "A trumpet of the thunder god is said to be rumored to be hidden in a nearby dungeon",
6: "A nature spirit has fallen in despair, and harvests will fail if she isn't found and newly inspired",
7: "A viral dance craze is actually a ritual, opening passages to another plane when performed well",
8: "War drums are sounding in the wilds, bringing a new level of organization to the evil tribes",
9: "A melancholic noble finds sound of cheer grating and seeks to plunge the world into shadow",
10: "A simple children's song may preserve secrets from a forgotten past",
11: "A mock battle of performances has kept the peace for years, but one side has begun cheating",
12: "A play seems to be about the party's past exploits, the final act predicts potential disaster",
13: "Someone or something is stealing all the ale, and that means smaller, less forgiving audiences.",
14: "A famous luthier is paying richly for rare woods and even more dangerous to obtain catgut",
15: "Suggestions from fans rarely provide good material, but occasionally provide adventure leads",
16: "An overeager artist's “immersive” performance experience proves dangerous for all",
17: "A forgotten verse to a popular song is uncovered, sparking a hunt for a legendary treasure",
18: "An ancient culture knew the secrets of harmonic levitation and built vast temples full of traps",
19: "A snake charmer got in over their head, it seems these were no ordinary snakes",
20: "The anthem celebrating the founder's heroism proves a complete fabrication, to the heir's chagrin",}

exile_drives = {1: "Achieve redemption for a past transgression",
2: "Reunite with lost loved ones",
3: "Find their way back home somehow",
4: "Restore their tarnished honor through deeds",
5: "Reclaim their rightful place from usurpers",
6: "Preserve the remnants of their dying culture",
7: "Prove innocence against false accusations",
8: "Discover a sense of belonging elsewhere",
9: "Establish a haven for other outcasts",
10: "Become a legendary hero out of spite",
11: "Serve others as an act of personal reform",
12: "Be an exemplary representative of their kind",
13: "Continue their pursuit of taboo knowledge",
14: "Demonstrate the power of second chances",
15: "Be true to self over cultural norms",
16: "Uphold the traditions of lost homeland",
17: "Avenge their lost loved ones and way of life",
18: "Earn their place within a new community",
19: "Balance out the past wrongs haunting them",
20: "Embrace the whims of destiny guiding them",}
exile_catalysts = {1: "Rumors of a lost relic from their homeland",
2: "Discovering a cryptic note from their past",
3: "Hints of a shot at redemption or vindication",
4: "A prophetic story told by their people",
5: "Unrest at home has rippling consequences",
6: "Deity speaks to them but they're labeled a heretic",
7: "The threat that destroyed their home returns",
8: "A mentor who fled accusations of treason",
9: "A historical enemy seen in a new light",
10: "Campfire tales told by fellow travelers",
11: "Archaic writings in their native tongue",
12: "Magical messages from an old ally",}
exile_growth = {1: "Isolated individual, to member of community",
2: "Looking for a way back, yo moving forward",
3: "Slowly embracing the parts that got them shunned",
4: "From crisis of identity, to reinventing self",
5: "Stranger in a strange land, to fully assimilated",
6: "The triumphant return of the prodigal hero",
7: "Seeking to atone, to achieving self-forgiveness",
8: "Discovering purpose beyond their own plight",}
exile_friends = {1: "The Tattered Banner: Remnants of a squad who once served a fallen king together",
2: "Freewheeling Caravan: Traveling band on the fringes of society who welcome in strays",
3: "The Uncounted Number: Isolated order that traces its origins to an ancient religious schism",
4: "Ruinborn: Community of refugees from a shattered realm sharing support and knowledge",}
exile_assets = {1: "The Beggar King: Homeless panhandler who claims to be the heir to a faraway throne",
2: "Otho Cruz: Knowledgeable scholar with a fascination for foreign cultures",
3: "Haya Rose: Runs a boarding house where many in need find refuge and community",
4: "Byn Zokar: Wandering trader who can get just about anything for the right price",
5: "Salizar Swan: Smuggler who has transported everything, including fleeing people",
6: "“X”: Mysterious benefactor sending brief missives signed with a single letter X",}
exile_items = {1: "Badge of their former station, though the position was stripped from them",
2: "Compass of the Exile: Always points back to a home they're forbidden from returning to",
3: "Boots of Deception: Leave random and confusing footprints, making them hard to track",
4: "Coat of Belonging: Illusory magic allows it to change its appearance to match local garb",
5: "Babble Stone: Once per day grants ability to understand and speak any language for 1 hour",
6: "Lidded Eye Amulet: Protects against magic to scry on the wearer or sense their location",
7: "Draught of the Lotus Eater: The drinker of this potion won't remember the next 6 hours",
8: "Mind Reader's Ring: Attuned can detect the thoughts of those nearby three times per day",
9: "Staff of the Traveler: Once per day can double speed and jumping ability for 1 minute",
10: "Scabbardless Saber: +1 sword that deals double damage to creatures from 1 specific plane",}
exile_antagonists = {1: "Homefire Alliance: Fellow expats but from rival partisan group back home",
2: "The Gate Keepers: Believe foreign influences are a threat to their cultural heritage",
3: "Iron Edict: Advocates for banishment for minor infractions, who claim what's left behind",
4: "Guttersnipes: Band of pickpocketing children who see outsiders as easy targets",
5: "Sweet Asylum: Charity formed to help the displaced, but spends lavishly on “fundraisers”",
6: "Oath Keepers: Preserve ancient feud with the character's kind, though roots are forgotten",}
exile_rivals = {1: "Fallen Halls: Built by the character's ancestors ages ago, architecture reminiscent of home",
2: "Cloud Forest: Foggy rainforest where many have sought and found shelter over the years",
3: "The Metropolis: Sweeps up and accepts everyone in the anonymity of the throngs",
4: "Cave of Whispers: Illusions drawn from early memories lure the unwary to their doom",
5: "The Frozen Fens: Once inhabited, now a barren waste of mud and permafrost",
6: "The Grand Nexus: Arcane gates that once could open to anywhere with the proper control",}
exile_locs = {1: "Tall Elric: Tavernfly who distrusts foreigners and thinks its obvious everyone else should too",
2: "Burgher Takai: Minor official who seeks to gain more political support by targeting outsiders",
3: "Faive the Fabulous: Performer who sees anyone more exotic than them as competition",
4: "Spymaster Jiru: The reason the party always feels like it's being watched when in town",
5: "Zealot Woorel: Believes their deity was betrayed by main god of the character's people",
6: "Av'Yoram: Exile turned adventurer who resents perceived copying of their identity",}
exile_monsters = {1: "Pale Ones: Exiled underground long ago, their eyes have atrophied and noses grown",
2: "Banished Banshee: Vengeful spirit who died alone and far from their home",
3: "Six-footed Stalker: Fearsome magical beast native to their homeland",
4: "Medusa: Collects creatures of every type for her statue garden, and doesn't have one of you yet",
5: "Portcullis Creepers: Stealthy guardians that deny entry by setting elaborate traps",
6: "Mimicubus: Changes its appearance to be beautiful to viewer, to seduce and devour them",}
exile_plot_hooks = {1: "Others are committing the same infraction that led to their banishment",
2: "Saving the day would certainly ingratiate them to the people of their new found home",
3: "Rumors of an important cultural heirloom prove a flimsy ploy, but the question is why",
4: "An influx of migrants were forced from their homes by an emerging threat",
5: "A curse that swept through their people a generation ago has reappeared here and now",
6: "Ostracized for their forbidden love, an orc and goblin seek to overthrow their tyrannical leader",
7: "A shadowy version of their homeland in an alternate dimension holds a powerful artifact",
8: "The child heir must be defended and hidden from the usurper's assassins until they come of age",
9: "A shooting star makes impact nearby, carrying outcasts from another world",
10: "A long lost friend tried to find them, but got dragged into a dangerous dungeon on the way",
11: "The one who finds the ancient scrolls in the ruins could start a new life on their terms",
12: "The locals adhere to a prophecy that implicates the character as a mythical hero reborn",
13: "A splintered sect of their people offer them a place in their plot for revenge, which could doom all",
14: "The whispers they're enemy spies stem from ignorance, but there's one sure way to end them",
15: "Outsider status makes them able to mediate between the feuding factions, or to tip the balance",
16: "The necromancer does not care who you are or where you come from, only that you serve",
17: "Last time one of your kind came through they were headed for the dungeon, and never returned",
18: "Turns outs this sympathetic wizard who is also an outcast was exiled for good reason",
19: "An unknown agent is sending progressively more dangerous threats after the party",
20: "A secretive order approaches the party with shiny gold and murky motives",}

explorer_drives = {1: "Literally put their name on the map",
2: "See things no one else alive has ever seen",
3: "Uncover lost secrets from ancient empires",
4: "Build evidence for their controversial theory",
5: "Amass a collection of rare artifacts to exhibit",
6: "Discover new species of flora and fauna",
7: "Chart the unknown and share knowledge",
8: "Track down the truth behind the legends",
9: "Inspire others to never settle for mundane",
10: "Continue in the footsteps a lost mentor",
11: "Establish contact with unique cultures",
12: "Witness what lies beyond the frontier",
13: "Escape a dark past by keeping it moving",
14: "Learn all that there is to learn",
15: "Surpass the exploits of a historical figure",
16: "Protect and reclaim ancient sites",
17: "Find that ineffable something they seek",
18: "Test themself against hostile environments",
19: "Reveal the buried origins of their people",
20: "Nothing beats the thrill of the unknown",}
explorer_catalysts = {1: "An early fascination with maps as a child",
2: "A loved one wandered off never to be found",
3: "A strange artifact hinting at unknown culture",
4: "A notebook from a doomed expedition",
5: "Local legends containing threads of truth",
6: "Stumbled upon a dungeon entrance",
7: "Strange creature from somewhere far away",
8: "A previous life of enforced seclusion",
9: "Never truly feeling at home anywhere",
10: "Accidentally got lost and loved the novelty",
11: "Inherited a set of navigation tools",
12: "Visions of ancient wonders lying buried",}
explorer_growth = {1: "From exploiting discoveries, to preserving them",
2: "Fear of the unknown, to the embrace of it",
3: "Wanderlust, to desire for established home",
4: "Discovering it is the journey, not the destination",
5: "Seeking personal fame, to serving the culture",
6: "Valuing wealth, to valuing knowledge",
7: "Uncovering personal connections to the past",
8: "Reckless risk taker, to careful strategist",}
explorer_friends = {1: "Carte Blanche: Cartographers guild willing to pay for information that expands their maps",
2: "Armchair Adventurers: Scholars who study and meet to discuss ancient cultures",
3: "The Windswept: Tribal nomads who've wandered the wilds for generations",
4: "Sherpa Circle: Guides who help the rich mount, and survive, expeditions in harsh places",}
explorer_assets = {1: "Steed Windrider: Tamed and rode a griffin, has had a bird's eye view of the territory",
2: "“Badger” Rocksnout: Mineral prospector always on the hunt for the next mother lode",
3: "Fante Moonsinger: Herbalist who wanders far and wide on their foraging trips",
4: "Runo Oakleg: Retired sailor with endless stories, some of them are even true",
5: "The Masked Troubadour: Travels from town to town performing, never shows their face",
6: "Ouma Letsego: Wealthy widow whose husband never returned from an expedition",}
explorer_items = {1: "A weathered map with landmarks no one seems to recognize",
2: "Symbolic Rune Set: Pictograms that enable basic communication with intelligent beings",
3: "Binoculars of Piercing Sight: Can view through partial obscurity like smoke and fog",
4: "Boots of the Trailblazer: Ease traveling over difficult terrain, and are very difficult to track",
5: "Amulet of Endurance: Protects against extreme weather conditions and exhaustion",
6: "Satchel of Traveling Matt: Extradimensional bag that holds much while remaining light",
7: "Diadem of Orientation: Makes it nearly impossible to get lost while attuned",
8: "Periapt of the Pathfinder: Grants advantage while searching for traps and secret doors",
9: "Tiny Tent: Magically allows six creatures to get a safe nights sleep in any environment",
10: "Survivalist Rod: Conjures food and drink, can cure disease, poison, and exhaustion",}
explorer_antagonists = {1: "Ruin Raiders: Adventuring party that delves dungeons hard and carouses in town harder",
2: "History's Heritage: Uphold a reverence to a mythic past they believe should stay buried",
3: "The Black Stacks: Archivists that hoard secret knowledge and spread disinformation",
4: "Disc Worlders: Irrationally believe the world has an edge and crossing it will upset the gods",
5: "Prime Meridians: Created myriad novelty treasure maps that often mislead adventurers",
6: "Toll House Wardens: Guards that patrol the roads and collect steep fees for it from travelers",}
explorer_rivals = {1: "Gazetteer Cavern: Cave network covered in mysterious petroglyphs from long ago",
2: "Sunken Citadel: Mythical lost city filled with wonders, discovered at the bottom of the sea",
3: "Starfall Fields: Stretch of cratered plains where meteorites frequently land as if attracted",
4: "Clockwork Labyrinth: A dungeon that rearranges itself periodically, defying mapping",
5: "Fiery Forest: Seepage from another plane makes these woods unique, and dangerous",
6: "Shifting Sands: Vast desert with no roads or landmarks where winds reveal and rebury ruins",}
explorer_locs = {1: "Thurton Howl: Competitive explorer who tries to claim all new discoveries as his own",
2: "Teema Stormcaller: Claims the weather follows her whims and demands payment",
3: "Etsonia Thok: Crafts hoax archaeological finds and profits widely off of them",
4: "Bron Emberway: Retired explorer who sees this whole generation as a preening babies",
5: "Lord Sassou: Holds ancestral claim to the area and expects a percentage of all finds",
6: "Pastor Bitok: Is vocal that nothing good comes from adventurers poking around places",}
explorer_monsters = {1: "Rainforest Wraith: Lead travelers astray with dense fog and strange sounds",
2: "Abominable Mountain Ape: Legendary, reclusive creatures of immense strength",
3: "Threshold Sphinx: Use riddles and puzzles to determine worthiness to enter sacred sites",
4: "Ghostly Garrison: Long-dead defenders who employ military tactics to repel intruders",
5: "Fossilizing Ooze: Encase the unwary in petrifying stone and digest them into hollow statues",
6: "Nesting Drake: Draconic creatures who den in beautiful ruins crafted by others",}
explorer_plot_hooks = {1: "All that is written on that particular area of the map is “here there be dragons”",
2: "The expedition to find the previous lost expedition is also lost, generating mass speculation",
3: "Sailors and fishermen are reporting a strange island that wasn't there a few weeks ago",
4: "A famous adventurer's journal speaks of a mysterious door they could never get open",
5: "The empire has ambitions to expand and is outfitting parties to explore beyond its borders",
6: "A dark twisted jungle is said to hold a rare medicinal herb that can cure a spreading curse",
7: "A rich noble is paying well for specimens from far off lands to add to their collection",
8: "Establishing the museum was a noble idea, but it proved a very tempting target for robbers",
9: "The sky fortress passes over this time every year, though nobody knows who or what is up there",
10: "A sinkhole opens up revealing a vast underground network of caverns, some formed by tools",
11: "The town's main industry is outfitting adventurers who come to delve the dungeon, few return",
12: "The mountain's harsh environment has kept the temple at the top from being plundered",
13: "A priceless relic was on a ship that sank and several groups are racing to recover it",
14: "The river's source has never been discovered, but someone must find it now that it has dried up",
15: "Encoded in a children's rhyme is the location of a treasure beneath a well known monument",
16: "Stumbling on the underground temple was considered good luck, until it proved to be occupied",
17: "An esteemed chef has an open order for rare and exotic ingredients",
18: "The dimensional rift claimed much of the town, but opened up a whole new world to explore",
19: "A popular song about a magical treasure is enticing, and was carefully crafted to lure people in",
20: "A cataclysmic disaster has reshaped the world and rendered all existing maps obsolete",}

farmer_drives = {}
farmer_catalysts = {}
farmer_growth = {}
farmer_friends = {}
farmer_assets = {}
farmer_items = {}
farmer_antagonists = {}
farmer_rivals = {}
farmer_locs = {}
farmer_monsters = {}
farmer_plot_hooks = {}

folk_hero_drives = {}
folk_hero_catalysts = {}
folk_hero_growth = {}
folk_hero_friends = {}
folk_hero_assets = {}
folk_hero_items = {}
folk_hero_antagonists = {}
folk_hero_rivals = {}
folk_hero_locs = {}
folk_hero_monsters = {}
folk_hero_plot_hooks = {}

fortune_teller_drives = {}
fortune_teller_catalysts = {}
fortune_teller_growth = {}
fortune_teller_friends = {}
fortune_teller_assets = {}
fortune_teller_items = {}
fortune_teller_antagonists = {}
fortune_teller_rivals = {}
fortune_teller_locs = {}
fortune_teller_monsters = {}
fortune_teller_plot_hooks = {}

gambler_drives = {}
gambler_catalysts = {}
gambler_growth = {}
gambler_friends = {}
gambler_assets = {}
gambler_items = {}
gambler_antagonists = {}
gambler_rivals = {}
gambler_locs = {}
gambler_monsters = {}
gambler_plot_hooks = {}

gladiator_drives = {}
gladiator_catalysts = {}
gladiator_growth = {}
gladiator_friends = {}
gladiator_assets = {}
gladiator_items = {}
gladiator_antagonists = {}
gladiator_rivals = {}
gladiator_locs = {}
gladiator_monsters = {}
gladiator_plot_hooks = {}

gravedigger_drives = {}
gravedigger_catalysts = {}
gravedigger_growth = {}
gravedigger_friends = {}
gravedigger_assets = {}
gravedigger_items = {}
gravedigger_antagonists = {}
gravedigger_rivals = {}
gravedigger_locs = {}
gravedigger_monsters = {}
gravedigger_plot_hooks = {}

guard_drives = {}
guard_catalysts = {}
guard_growth = {}
guard_friends = {}
guard_assets = {}
guard_items = {}
guard_antagonists = {}
guard_rivals = {}
guard_locs = {}
guard_monsters = {}
guard_plot_hooks = {}

herbalist_drives = {}
herbalist_catalysts = {}
herbalist_growth = {}
herbalist_friends = {}
herbalist_assets = {}
herbalist_items = {}
herbalist_antagonists = {}
herbalist_rivals = {}
herbalist_locs = {}
herbalist_monsters = {}
herbalist_plot_hooks = {}

hunter_drives = {}
hunter_catalysts = {}
hunter_growth = {}
hunter_friends = {}
hunter_assets = {}
hunter_items = {}
hunter_antagonists = {}
hunter_rivals = {}
hunter_locs = {}
hunter_monsters = {}
hunter_plot_hooks = {}

knight_drives = {}
knight_catalysts = {}
knight_growth = {}
knight_friends = {}
knight_assets = {}
knight_items = {}
knight_antagonists = {}
knight_rivals = {}
knight_locs = {}
knight_monsters = {}
knight_plot_hooks = {}

laborer_drives = {}
laborer_catalysts = {}
laborer_growth = {}
laborer_friends = {}
laborer_assets = {}
laborer_items = {}
laborer_antagonists = {}
laborer_rivals = {}
laborer_locs = {}
laborer_monsters = {}
laborer_plot_hooks = {}

martial_disciple_drives = {}
martial_disciple_catalysts = {}
martial_disciple_growth = {}
martial_disciple_friends = {}
martial_disciple_assets = {}
martial_disciple_items = {}
martial_disciple_antagonists = {}
martial_disciple_rivals = {}
martial_disciple_locs = {}
martial_disciple_monsters = {}
martial_disciple_plot_hooks = {}

merchant_drives = {}
merchant_catalysts = {}
merchant_growth = {}
merchant_friends = {}
merchant_assets = {}
merchant_items = {}
merchant_antagonists = {}
merchant_rivals = {}
merchant_locs = {}
merchant_monsters = {}
merchant_plot_hooks = {}

medic_drives = {}
medic_catalysts = {}
medic_growth = {}
medic_friends = {}
medic_assets = {}
medic_items = {}
medic_antagonists = {}
medic_rivals = {}
medic_locs = {}
medic_monsters = {}
medic_plot_hooks = {}

miner_drives = {}
miner_catalysts = {}
miner_growth = {}
miner_friends = {}
miner_assets = {}
miner_items = {}
miner_antagonists = {}
miner_rivals = {}
miner_locs = {}
miner_monsters = {}
miner_plot_hooks = {}

noble_drives = {}
noble_catalysts = {}
noble_growth = {}
noble_friends = {}
noble_assets = {}
noble_items = {}
noble_antagonists = {}
noble_rivals = {}
noble_locs = {}
noble_monsters = {}
noble_plot_hooks = {}

nomad_drives = {}
nomad_catalysts = {}
nomad_growth = {}
nomad_friends = {}
nomad_assets = {}
nomad_items = {}
nomad_antagonists = {}
nomad_rivals = {}
nomad_locs = {}
nomad_monsters = {}
nomad_plot_hooks = {}

outlander_drives = {}
outlander_catalysts = {}
outlander_growth = {}
outlander_friends = {}
outlander_assets = {}
outlander_items = {}
outlander_antagonists = {}
outlander_rivals = {}
outlander_locs = {}
outlander_monsters = {}
outlander_plot_hooks = {}

pirate_drives = {}
pirate_catalysts = {}
pirate_growth = {}
pirate_friends = {}
pirate_assets = {}
pirate_items = {}
pirate_antagonists = {}
pirate_rivals = {}
pirate_locs = {}
pirate_monsters = {}
pirate_plot_hooks = {}

pilgrim_drives = {}
pilgrim_catalysts = {}
pilgrim_growth = {}
pilgrim_friends = {}
pilgrim_assets = {}
pilgrim_items = {}
pilgrim_antagonists = {}
pilgrim_rivals = {}
pilgrim_locs = {}
pilgrim_monsters = {}
pilgrim_plot_hooks = {}

prisoner_drives = {}
prisoner_catalysts = {}
prisoner_growth = {}
prisoner_friends = {}
prisoner_assets = {}
prisoner_items = {}
prisoner_antagonists = {}
prisoner_rivals = {}
prisoner_locs = {}
prisoner_monsters = {}
prisoner_plot_hooks = {}

sage_scholar_drives = {}
sage_scholar_catalysts = {}
sage_scholar_growth = {}
sage_scholar_friends = {}
sage_scholar_assets = {}
sage_scholar_items = {}
sage_scholar_antagonists = {}
sage_scholar_rivals = {}
sage_scholar_locs = {}
sage_scholar_monsters = {}
sage_scholar_plot_hooks = {}

sailor_drives = {}
sailor_catalysts = {}
sailor_growth = {}
sailor_friends = {}
sailor_assets = {}
sailor_items = {}
sailor_antagonists = {}
sailor_rivals = {}
sailor_locs = {}
sailor_monsters = {}
sailor_plot_hooks = {}

scout_drives = {}
scout_catalysts = {}
scout_growth = {}
scout_friends = {}
scout_assets = {}
scout_items = {}
scout_antagonists = {}
scout_rivals = {}
scout_locs = {}
scout_monsters = {}
scout_plot_hooks = {}

soldier_drives = {}
soldier_catalysts = {}
soldier_growth = {}
soldier_friends = {}
soldier_assets = {}
soldier_items = {}
soldier_antagonists = {}
soldier_rivals = {}
soldier_locs = {}
soldier_monsters = {}
soldier_plot_hooks = {}

spy_drives = {}
spy_catalysts = {}
spy_growth = {}
spy_friends = {}
spy_assets = {}
spy_items = {}
spy_antagonists = {}
spy_rivals = {}
spy_locs = {}
spy_monsters = {}
spy_plot_hooks = {}

teacher_drives = {}
teacher_catalysts = {}
teacher_growth = {}
teacher_friends = {}
teacher_assets = {}
teacher_items = {}
teacher_antagonists = {}
teacher_rivals = {}
teacher_locs = {}
teacher_monsters = {}
teacher_plot_hooks = {}

tinker_drives = {}
tinker_catalysts = {}
tinker_growth = {}
tinker_friends = {}
tinker_assets = {}
tinker_items = {}
tinker_antagonists = {}
tinker_rivals = {}
tinker_locs = {}
tinker_monsters = {}
tinker_plot_hooks = {}

urchin_drives = {}
urchin_catalysts = {}
urchin_growth = {}
urchin_friends = {}
urchin_assets = {}
urchin_items = {}
urchin_antagonists = {}
urchin_rivals = {}
urchin_locs = {}
urchin_monsters = {}
urchin_plot_hooks = {}

warrior_drives = {}
warrior_catalysts = {}
warrior_growth = {}
warrior_friends = {}
warrior_assets = {}
warrior_items = {}
warrior_antagonists = {}
warrior_rivals = {}
warrior_locs = {}
warrior_monsters = {}
warrior_plot_hooks = {}

weirdo_drives = {}
weirdo_catalysts = {}
weirdo_growth = {}
weirdo_friends = {}
weirdo_assets = {}
weirdo_items = {}
weirdo_antagonists = {}
weirdo_rivals = {}
weirdo_locs = {}
weirdo_monsters = {}
weirdo_plot_hooks = {}

continue_prompt = ""  # Initialize a loop continuation variable.
while continue_prompt!="q":
    dice_count = input_number("How many dice? ")
    sides_count = input_number("How many sides to dice? ")
    dice_list = throw_dice(dice_count, sides_count)
    print(f"List of the dice thrown: {dice_list}.")
    print("Press enter to continue or type 'q' to quit.")
    continue_prompt = input()
