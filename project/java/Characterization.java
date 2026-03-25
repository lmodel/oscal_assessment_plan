package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A collection of descriptive data about the containing object from a specific origin.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Characterization  {

  private Origin origin;
  private List<Facet> facets;
  private List<Property> props;
  private List<Link> links;

}