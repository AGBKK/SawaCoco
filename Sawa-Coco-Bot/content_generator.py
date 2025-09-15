import openai
import random
import json
from typing import List, Dict
from config import Config

class ContentGenerator:
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.company_name = Config.COMPANY_NAME
        self.main_product = Config.MAIN_PRODUCT
        self.website_url = Config.WEBSITE_URL
        self.company_location = Config.COMPANY_LOCATION
        self.company_focus = Config.COMPANY_FOCUS
        
        # Content templates and topics for Sawa Coco products
        self.content_topics = [
            # MCT Oil & Powder topics
            "health_benefits",
            "usage_tips",
            "science_facts",
            "recipes",
            "fitness_performance",
            "weight_management",
            "brain_health",
            "energy_boost",
            "ketogenic_diet",
            "product_features",
            # Charcoal topics
            "charcoal_benefits",
            "charcoal_applications",
            "charcoal_quality",
            "bbq_grilling",
            "shisha_hookah",
            "industrial_uses",
            # General topics
            "sustainability",
            "palm_free_benefits",
            "coconut_sourcing",
            "b2b_applications",
            "clean_farming",
            "zero_waste"
        ]
        
        self.post_types = [
            "educational",
            "testimonial",
            "tip",
            "fact",
            "recipe",
            "motivation",
            "comparison",
            "how_to"
        ]

    def generate_post_content(self, topic: str = None, post_type: str = None) -> Dict[str, str]:
        """Generate a single post about MCT Oil"""
        if not topic:
            topic = random.choice(self.content_topics)
        if not post_type:
            post_type = random.choice(self.post_types)
        
        prompt = self._create_prompt(topic, post_type)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a health and wellness content creator specializing in MCT Oil products. Create engaging, informative social media posts."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            content = response.choices[0].message.content.strip()
            
            # Add hashtags and company mention with CTA
            hashtags = self._generate_hashtags(topic)
            cta = self._get_call_to_action(topic)
            final_content = f"{content}\n\n{hashtags}\n\n🥥 {self.company_name} - {self.main_product}\n🌍 Sustainable sourcing from {self.company_location}\n\n{cta}\n{self.website_url}"
            
            return {
                "content": final_content,
                "topic": topic,
                "post_type": post_type,
                "hashtags": hashtags
            }
            
        except Exception as e:
            # Fallback content if API fails
            return self._get_fallback_content(topic, post_type)

    def _create_prompt(self, topic: str, post_type: str) -> str:
        """Create a prompt for content generation"""
        prompts = {
            "health_benefits": f"Write a {post_type} post about the health benefits of premium coconut-based MCT Oil. Focus on scientific benefits and practical applications.",
            "usage_tips": f"Create a {post_type} post with practical tips on how to use MCT Oil effectively in daily routine for optimal results.",
            "science_facts": f"Write a {post_type} post sharing interesting scientific facts about MCT Oil and medium-chain triglycerides from coconut sources.",
            "recipes": f"Create a {post_type} post featuring a simple recipe that incorporates premium MCT Oil or MCT powder.",
            "fitness_performance": f"Write a {post_type} post about how coconut-based MCT Oil can enhance athletic performance and workout results.",
            "weight_management": f"Create a {post_type} post about MCT Oil's role in healthy weight management and metabolism support.",
            "brain_health": f"Write a {post_type} post about MCT Oil's cognitive benefits and brain health support from pure coconut sources.",
            "energy_boost": f"Create a {post_type} post about how premium MCT Oil provides clean, sustained energy throughout the day.",
            "ketogenic_diet": f"Write a {post_type} post about MCT Oil's importance in ketogenic and low-carb diets, focusing on C8/C10 benefits.",
            "product_features": f"Create a {post_type} post highlighting the quality and features of Sawa Coco's premium MCT Oil products (60/40 blend and C8/98).",
            # Charcoal content prompts
            "charcoal_benefits": f"Write a {post_type} post about the benefits of premium coconut shell charcoal over regular charcoal - clean burn, minimal ash, long-lasting.",
            "charcoal_applications": f"Create a {post_type} post about the various applications of coconut shell charcoal: shisha, BBQ, industrial uses.",
            "charcoal_quality": f"Write a {post_type} post about Sawa Coco's high-grade coconut shell charcoal quality standards and production process in Thailand.",
            "bbq_grilling": f"Create a {post_type} post about using coconut shell charcoal for BBQ and grilling - superior heat, clean taste, eco-friendly.",
            "shisha_hookah": f"Write a {post_type} post about premium coconut shell charcoal for shisha/hookah - minimal smoke, long burn time, pure flavor.",
            "industrial_uses": f"Create a {post_type} post about industrial applications of coconut shell charcoal and its export quality standards.",
            # General topics
            "sustainability": f"Write a {post_type} post about sustainable coconut sourcing and environmental responsibility across all Sawa Coco products.",
            "palm_free_benefits": f"Create a {post_type} post about the benefits of 100% palm-free production and why coconut-based is superior.",
            "coconut_sourcing": f"Write a {post_type} post about single-origin coconut sourcing from Thailand and clean farming practices.",
            "b2b_applications": f"Create a {post_type} post about Sawa Coco's B2B applications for food brands, supplement manufacturers, and industrial clients.",
            "clean_farming": f"Write a {post_type} post about chemical-free, pesticide-free coconut farming and its impact on product purity.",
            "zero_waste": f"Write a {post_type} post about Sawa Coco's zero-waste approach - using coconuts for MCT oil AND shells for premium charcoal."
        }
        
        base_prompt = prompts.get(topic, f"Write a {post_type} post about premium coconut-based MCT Oil.")
        return f"{base_prompt} Keep it engaging, informative, and under 250 words. Include emojis where appropriate. Mention that this is from Thailand's sustainable coconut farms when relevant."

    def _generate_hashtags(self, topic: str) -> str:
        """Generate relevant hashtags for the post"""
        base_hashtags = ["#MCTOil", "#SawaCoco", "#CoconutBased", "#Thailand"]
        
        topic_hashtags = {
            "health_benefits": ["#HealthBenefits", "#NaturalHealth", "#Wellness"],
            "usage_tips": ["#HealthTips", "#WellnessTips", "#MCTTips"],
            "science_facts": ["#HealthScience", "#MCTScience", "#Nutrition"],
            "recipes": ["#HealthyRecipes", "#MCTRecipes", "#Cooking"],
            "fitness_performance": ["#Fitness", "#Performance", "#WorkoutFuel"],
            "weight_management": ["#WeightLoss", "#Metabolism", "#HealthyWeight"],
            "brain_health": ["#BrainHealth", "#Cognitive", "#MentalWellness"],
            "energy_boost": ["#Energy", "#NaturalEnergy", "#CleanEnergy"],
            "ketogenic_diet": ["#Keto", "#KetogenicDiet", "#LowCarb"],
            "product_features": ["#PremiumMCT", "#QualityProducts", "#C8C10"],
            "sustainability": ["#Sustainable", "#EcoFriendly", "#ResponsibleSourcing"],
            "palm_free_benefits": ["#PalmFree", "#CoconutOnly", "#CleanProducts"],
            "coconut_sourcing": ["#SingleOrigin", "#ThailandCoconuts", "#QualitySourcing"],
            "b2b_applications": ["#B2B", "#BulkSupplier", "#FoodIndustry"],
            "clean_farming": ["#CleanFarming", "#NoPesticides", "#OrganicFarming"],
            # Charcoal hashtags
            "charcoal_benefits": ["#CoconutCharcoal", "#PremiumCharcoal", "#CleanBurn"],
            "charcoal_applications": ["#Charcoal", "#BBQ", "#Shisha"],
            "charcoal_quality": ["#HighGrade", "#QualityControl", "#ExportQuality"],
            "bbq_grilling": ["#BBQ", "#Grilling", "#EcoFriendly"],
            "shisha_hookah": ["#Shisha", "#Hookah", "#MinimalSmoke"],
            "industrial_uses": ["#Industrial", "#Export", "#B2BCharcoal"],
            "zero_waste": ["#ZeroWaste", "#Sustainable", "#CircularEconomy"]
        }
        
        specific_hashtags = topic_hashtags.get(topic, ["#Health"])
        all_hashtags = base_hashtags + specific_hashtags
        
        return " ".join(all_hashtags[:8])  # Limit to 8 hashtags

    def _get_call_to_action(self, topic: str) -> str:
        """Generate topic-specific call-to-action"""
        cta_options = {
            # MCT Oil CTAs
            "health_benefits": "💪 Ready to boost your energy? Contact us for bulk MCT oil pricing!",
            "usage_tips": "☕ Want to try premium MCT oil? Get wholesale rates for your business!",
            "science_facts": "🧠 Interested in our C8/98 ultra-pure MCT oil? Request samples today!",
            "recipes": "👨‍🍳 Perfect for food brands! Get bulk MCT oil & powder pricing!",
            "fitness_performance": "🏋️ Fuel your customers' performance! Wholesale MCT oil available!",
            "weight_management": "⚖️ Help your clients succeed! Partner with us for premium MCT products!",
            "brain_health": "🧠 Boost your product line! Contact us for MCT oil & powder solutions!",
            "energy_boost": "⚡ Power up your brand! Get competitive bulk MCT oil rates!",
            "ketogenic_diet": "🥑 Perfect for keto brands! Wholesale C8/C10 & C8/98 MCT oils available!",
            "product_features": "✨ Ready to source premium MCT products? Contact our B2B team!",
            
            # Charcoal CTAs  
            "charcoal_benefits": "🔥 Upgrade your charcoal supply! Export-quality coconut shell charcoal available!",
            "charcoal_applications": "🍖 Perfect for your business! Bulk coconut shell charcoal - contact us!",
            "charcoal_quality": "🏆 Need premium charcoal? Get Thailand export-quality pricing today!",
            "bbq_grilling": "🔥 Stock the best! Wholesale coconut shell charcoal for retailers!",
            "shisha_hookah": "💨 Premium shisha charcoal supplier! Contact us for bulk orders!",
            "industrial_uses": "🏭 Industrial charcoal needs? We supply export-quality coconut shell charcoal!",
            
            # General CTAs
            "sustainability": "🌱 Partner with sustainable suppliers! Contact Sawa Coco B2B team!",
            "palm_free_benefits": "🌿 Go palm-free! Source 100% coconut-based products with us!",
            "coconut_sourcing": "🥥 Direct from Thailand farms! Get premium coconut product pricing!",
            "b2b_applications": "🤝 Ready to partner? Contact our B2B team for custom solutions!",
            "clean_farming": "🌾 Clean products for clean brands! Get wholesale pricing today!",
            "zero_waste": "♻️ Complete coconut solutions! MCT oils + charcoal - contact us!"
        }
        
        return cta_options.get(topic, "🌟 Discover premium coconut products! Contact us for B2B pricing!")

    def _get_fallback_content(self, topic: str, post_type: str) -> Dict[str, str]:
        """Fallback content when API is unavailable"""
        fallback_posts = {
            "health_benefits": "🥥 Premium coconut-based MCT Oil from Thailand delivers rapid energy and metabolism support! Our sustainable sourcing ensures pure, clean nutrition for your wellness journey. ⚡",
            "usage_tips": "💡 Pro tip: Start with 1 tsp of our premium MCT Oil in coffee or smoothies. Our 60/40 C8/C10 blend provides optimal absorption and sustained energy! ☕",
            "science_facts": "🧠 Science fact: Our C8/98 MCT Oil converts directly to ketones, bypassing normal digestion for immediate brain fuel! Pure coconut sourcing from Thailand's clean farms. 🔬",
            "sustainability": "🌍 100% palm-free, sustainably sourced from single-origin Thai coconut farms. Zero chemicals, zero pesticides - just pure, responsible products! 🥥",
            "product_features": "✨ Sawa Coco offers premium MCT oils: 60/40 blend for versatility, C8/98 for performance. Plus MCT powder for easy mixing! All from Thailand's finest coconuts. 🏆",
            "charcoal_benefits": "🔥 Premium coconut shell charcoal burns cleaner, longer, and produces minimal ash compared to regular charcoal. Perfect for BBQ, shisha, and industrial use! 🥥",
            "bbq_grilling": "🍖 Elevate your BBQ game with coconut shell charcoal! Superior heat retention, clean taste, and eco-friendly. Made from Thailand's finest coconut shells. 🔥",
            "shisha_hookah": "💨 Premium coconut shell charcoal for the perfect shisha experience - minimal smoke, long burn time, pure flavor. Export quality from Thailand! 🥥",
            "zero_waste": "♻️ From coconut to MCT oil to premium charcoal - Sawa Coco's zero-waste approach maximizes every part of Thailand's sustainable coconuts! 🌱"
        }
        
        content = fallback_posts.get(topic, "🥥 Discover Sawa Coco's premium coconut products from Thailand - MCT Oils, MCT Powders & Coconut Shell Charcoal! 💪")
        hashtags = self._generate_hashtags(topic)
        
        cta = self._get_call_to_action(topic)
        return {
            "content": f"{content}\n\n{hashtags}\n\n🥥 {self.company_name} - {self.main_product}\n🌍 Sustainable sourcing from {self.company_location}\n\n{cta}\n{self.website_url}",
            "topic": topic,
            "post_type": post_type,
            "hashtags": hashtags
        }

    def generate_daily_content_batch(self, count: int = 4) -> List[Dict[str, str]]:
        """Generate multiple posts for the day"""
        posts = []
        used_topics = set()
        
        for _ in range(count):
            # Ensure variety by not repeating topics
            available_topics = [t for t in self.content_topics if t not in used_topics]
            if not available_topics:
                used_topics.clear()
                available_topics = self.content_topics
            
            topic = random.choice(available_topics)
            used_topics.add(topic)
            
            post = self.generate_post_content(topic)
            posts.append(post)
        
        return posts
