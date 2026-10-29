use crawlora_kick::{Client, KickCategoriesParams, ModelKickCategoriesResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.kick.categories(Default::default()).await?;
    let data: ModelKickCategoriesResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
