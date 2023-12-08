from api.models import Factors,Information,Solutions
Factors.objects.all().delete()
Information.objects.all().delete()
Solutions.objects.all().delete()

climate_factors = {
    "Greenhouse Gas Emissions":  "Greenhouse gases (GHGs) are gases that trap heat in the Earth's atmosphere. GHG emissions are the main cause of climate change.",
    "Deforestation":  "Deforestation is the process of converting forests to other land uses, such as agriculture, logging, or urbanization.",
    "Use of Ozone-Depleting Substances (ODS)":  "Ozone-depleting substances (ODS) are substances that destroy the ozone layer, a natural shield that protects the Earth from harmful ultraviolet rays from the sun.",
    "Urbanization":  "Urbanization is the process of cities and urban areas growing.",
    "Intensive Agriculture":  "Intensive agriculture is a form of agriculture that uses modern techniques and technologies to produce large quantities of food."
}




for factor_name,desc in climate_factors.items():
    factor = Factors.objects.create(
        name = factor_name,
        description = desc
    )

climate_facts = {
    # True Facts
    "Rising Global Temperatures": {
        "description": "The average global temperature has increased by about 1 degree Celsius since the late 19th century."
    },
    "Human-Caused Warming": {
        "description": "Most of the current warming trend is extremely likely (greater than 95% probability) the result of human activity since the 1950s."
    },
    "Accelerating Warming Trend": {
        "description": "The rate of warming is accelerating, with the five warmest years on record occurring since 2010."
    },
    "IPCC Report": {
        "description": "The Intergovernmental Panel on Climate Change (IPCC) concluded in its Fifth Assessment Report that it is extremely likely that human influence has been the dominant cause of the observed warming since the mid-20th century."
    },
    "Rising Sea Levels": {
        "description": "Sea levels are rising at an increasing rate, driven by thermal expansion of the oceans and melting glaciers and ice sheets."
    },
    "Extreme Weather Events": {
        "description": "The frequency and intensity of extreme weather events, such as heatwaves, droughts, floods, and wildfires, are increasing as a result of climate change."
    },
    "Melting Arctic Sea Ice": {
        "description": "The Arctic sea ice is melting at an alarming rate, with the extent of the ice cap in September declining by about 12% per decade since the 1970s."
    },
    "Impact on Ecosystems": {
        "description": "Climate change is having a significant impact on ecosystems around the world, leading to species loss, habitat destruction, and changes in plant and animal distributions."
    },
    "Human Impacts of Climate Change": {
        "description": "The impacts of climate change are already being felt by people around the world, including through loss of life, displacement, and damage to infrastructure."
    },
    "Time for Action": {
        "description": "There is still time to take action to mitigate climate change and reduce its impacts, but the window of opportunity is closing."
    },
    "Ocean Absorbing Carbon Dioxide": {
        "description": "The ocean absorbs about 25% of the carbon dioxide emitted by human activities, which is causing the ocean to become more acidic."
    },
    "Ocean Acidification": {
        "description": "The acidity of the ocean has increased by about 30% since the beginning of the industrial revolution."
    },
    "Acidification Impacts": {
        "description": "Ocean acidification is harming marine life, including coral reefs, shellfish, and fish."
    },
    "Melting Glaciers and Freshwater": {
        "description": "The melting of glaciers and ice sheets is contributing to sea level rise and is also causing changes in freshwater availability."
    },
    "Changing Precipitation Patterns": {
        "description": "Changes in precipitation patterns are leading to increased droughts in some regions and floods in others."
    },
    "Exacerbating Inequalities": {
        "description": "Climate change is exacerbating existing inequalities and vulnerabilities, disproportionately impacting low-income communities and developing countries."
    },
    "Transition to Renewable Energy": {
        "description": "The transition to renewable energy sources is essential for reducing greenhouse gas emissions and mitigating climate change."
    },
    "Energy Efficiency Measures": {
        "description": "Energy efficiency measures, such as improving building insulation and using energy-efficient appliances, can also help to reduce greenhouse gas emissions."
    },
    "Individual Actions": {
        "description": "Individual actions, such as reducing energy consumption, choosing sustainable products, and eating less meat, can contribute to climate change mitigation."
    },
    "Public Discourse and Advocacy": {
        "description": "It is important to engage in public discourse and advocacy to raise awareness about climate change and demand action from governments and businesses."
    },
}
false_climate_facts = {
    # False Facts
    "Natural Phenomenon": {
        "description": "Climate change is a natural phenomenon and human activity has no significant impact."
    },
    "Global Warming Stopped/Reversed": {
        "description": "Global warming has stopped or reversed in recent years."
    },
    "Natural Cycle": {
        "description": "The Earth's climate has always changed and the current warming trend is just part of a natural cycle."
    },
    "IPCC Unreliable": {
        "description": "The IPCC is not a credible source of information on climate change and its reports are biased."
    },
    "Costs Outweigh Benefits": {
        "description": "Climate change is not a serious threat and the costs of taking action to mitigate it outweigh the benefits."
    },
    "Renewables Unreliable/Unaffordable": {
        "description": "Renewable energy sources are not reliable or affordable and cannot replace fossil fuels."
    },
    "Individual Actions Ineffective": {
        "description": "Individual actions to reduce greenhouse gas emissions will not make a difference."
    },
    "Climate Change Hoax": {
        "description": "Climate change is a hoax created by scientists and environmentalists to gain funding and attention."
    },
    "Geoengineering Solution": {
        "description": "Geoengineering, such as solar radiation management, can easily solve climate change without the need to reduce greenhouse gas emissions."
    },
    "Adaptation Easier than Mitigation": {
        "description": "Adapting to climate change is easier and more cost-effective than mitigating it."
    },
    "Plants Benefit from CO2": {
        "description": "Plants benefit from increased CO2 levels and will thrive in a warmer world."
    },
    "Natural Factors Cause Warming": {
        "description": "The warming trend is mainly due to natural factors like solar activity and volcanic eruptions."
    },
    "Climate Change Benefits": {
        "description": "Climate change will bring more benefits than harms, such as longer growing seasons and more rainfall in some regions."
    },
    "Nuclear Energy Solution": {
        "description": "Nuclear energy is a clean and reliable alternative to fossil fuels and can solve climate change without the need for renewables."
    },
    "Climate Models Unreliable": {
        "description": "Climate models are unreliable and cannot accurately predict future climate change."
    },
    "No Scientific Consensus": {
        "description": "There is no scientific consensus on the causes and impacts of climate change."
    },
    "Distraction from Other Issues": {
        "description": "The focus on climate change distracts from other important environmental issues like air and water pollution."
    },
    "Depopulation Solution": {
        "description": "Depopulation is the most effective solution to mitigate climate change."
    },
    "Developing Countries Exempt": {
        "description": "Developing countries should not be held accountable for reducing their greenhouse gas emissions until developed countries have done more."
    },
    "Climate Change Conspiracy": {
        "description": "Climate change is a conspiracy designed to control populations and economies."
    },
}


for fact,desc in climate_facts.items():
    Information.objects.create(
        title = fact ,
        description = desc["description"],
        is_true= True
    )

for fact,desc in false_climate_facts.items():
    Information.objects.create(
        title = fact ,
        description = desc["description"],
        is_true= False
    )
t_solutions = {
    "United Nations Climate Change Conference": {
        "desc": "International summits that bring together world leaders to discuss climate change and measures to mitigate it.",
        "img": "https://climatepromise.undp.org/sites/default/files/inline-images/Banner%20FR.jpg",
        "date": ""
    },
    "Global Climate March": {
        "desc": "Climate marches are events organized by citizens worldwide to protest against climate change and urge governments to take action.",
        "img": "https://www.novethic.fr/fileadmin/Manifestation-climat-australie-JennyEvans-Getty-AFP.jpg",
        "date": ""
    },
    "World Energy Day": {
        "desc": "This event aims to raise awareness about global energy challenges and promote the use of renewable energy sources.",
        "img": "https://groupe-synergys.fr/wp-content/uploads/2023/10/journee_energie-scaled.jpg",
        "date": "October 22"
    },
    "World Environment Day": {
        "desc": "Organized by the United Nations, this day aims to raise awareness about crucial environmental issues, including climate change. Each year, a specific theme is chosen to encourage positive actions.",
        "img": "https://www.peaceandcooperation.org/wp-content/uploads/2021/06/Journ%C3%A9e-mondiale-de-lenvironnement.jpg",
        "date": "June 5"
    },
    "Sustainable Development Week": {
        "desc": "This week highlights efforts to promote sustainable development and raise awareness about environmental issues.",
        "img": "https://actus.zoobeauval.com/wp-content/uploads/2019/06/actuzoo_semaine_developpement_durable_2019_1200x800-750x500.jpg",
        "date": ""
    },
    "Earth Hour": {
        "desc": "A global movement encouraged by the World Wide Fund for Nature (WWF), Earth Hour urges individuals, businesses, and governments to turn off their lights for one hour to show their commitment to the fight against climate change.",
        "img": "https://www.urbanwoods.net/wp-content/uploads/2021/03/4948178.jpg",
        "date": ""
    },
    "Earth Hour": {
        "desc": "A global movement encouraged by the World Wide Fund for Nature (WWF), Earth Hour urges individuals, businesses, and governments to turn off their lights for one hour to show their commitment to the fight against climate change.",
        "img": "https://www.urbanwoods.net/wp-content/uploads/2021/03/4948178.jpg",
        "date": ""
    },
}
for sol,dic in t_solutions.items():
    Solutions.objects.create(
        title = sol ,
        desription = dic["desc"],
        date= dic["date"],
        image= dic["img"]
    )

