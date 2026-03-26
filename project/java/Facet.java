package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  An individual characteristic that is part of a larger set produced by the same actor.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Facet  {

  private String name;
  private String value;
  private String system;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}