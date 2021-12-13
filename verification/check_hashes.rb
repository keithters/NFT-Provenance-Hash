# Given the provided image_hashes.csv (from the Turf crew), this is a Ruby
# script that let's you verify it yourself, assuming you have downloaded the images locally.

require 'digest'
require 'csv'

found_bad_matches = false
all_hashes = ''

CSV.foreach("provenance_record.csv", headers: true) do |row|
  filename 		= row[0]  
  image_hash  = row[1]


  our_hash = Digest::SHA256.hexdigest File.read(filename)
  if our_hash != image_hash
    puts "❌: Hashes do not match for #{filename}!"
    found_bad_matches = true
  end

  all_hashes << image_hash

end

if !found_bad_matches
  puts "✅: All the individual image hashes matched!"
  puts "🖌️: Provenance Hash: #{Digest::SHA256.hexdigest(all_hashes)}"
end