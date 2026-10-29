require_relative "lib/crawlora/kick/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-kick"
  spec.version = Crawlora::Kick::VERSION
  spec.summary = "Kick API client for Crawlora (21 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Kick API. Covers channels, livestreams, clips, categories, search, and public mobile-app catalogues across 21 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=kick-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-kick", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-kick/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
