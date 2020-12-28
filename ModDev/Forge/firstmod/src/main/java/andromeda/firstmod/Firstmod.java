package andromeda.firstmod;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import andromeda.firstmod.lists.ItemList;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod("firstmod")

public class Firstmod {
	
	public static Firstmod instance;
	public static final String modid = "firstmod";
	private static final Logger logger = LogManager.getLogger(modid);
	
	public Firstmod() {
		instance = this;
//		these two lines listen for the setup and clientreg functions
		FMLJavaModLoadingContext.get().getModEventBus().addListener(this::setup);
		FMLJavaModLoadingContext.get().getModEventBus().addListener(this::clientRegistries);
//		makes forge register this file
		MinecraftForge.EVENT_BUS.register(this);
	}
	
	private void setup(final FMLCommonSetupEvent event) {
		logger.info("setup method registered ;)");
		
	}
	
	private void clientRegistries(final FMLClientSetupEvent event) {
		logger.info("clientRegistries method registered ;)");
		
	}
	
	@Mod.EventBusSubscriber(bus=Mod.EventBusSubscriber.Bus.MOD)
//	This is where we register items, runs with setup and clientregirstries
	public static class RegistryEvents{
		
		@SubscribeEvent
		public static void registerItems(final RegistryEvent.Register<Item> event){
			
			logger.info("registerItems method registered");
			 
			event.getRegistry().registerAll
			(
//				here we are registering the item tutorial_item as a new item with (...) properties
//				the .group(...) gives us the creative tab that the item will be under
//				note that the name comes after the Item() group
//					we can add as many items as we want, as long as they are all seperated by a comma
					ItemList.tutorial_item = new Item(new Item.Properties().group(ItemGroup.MISC)).setRegistryName(new ResourceLocation(modid, "tutorial_item")),
					ItemList.tutorial_item = new Item(new Item.Properties().group(ItemGroup.MISC)).setRegistryName(location("tutorial_item2"))

			);
		}
//		a function to clean up the above decleration, so we can just do .setRegistryName(location(name)
		private static ResourceLocation location(String name) {
			return new ResourceLocation(modid, name);
		}
		
	}


}
